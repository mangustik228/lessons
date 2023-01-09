# MODE=1 сохранит как в тз 4.8.2
# MODE=2 сохранит всю информацию выкаченную
# MODE=4 сохранит как в тз 4.8.4
# PARSE_PRODUCTS = можно указать кол-во товаров которое спарсить(если медленный интернет и лень ждать когда спарситься все). Если значение None, то парсится все
# SAVE_BY_ID сохраняет в бд по названию указанному в атрибуте id, иначе по русскому названию
# TREE_DESCRIPTION описание description будет древовидным(работает только если указан OUTPUT="json")
# Писать ли ссылку на товар в выходной файл

import pandas as pd
from parsel import Selector
import requests
from tqdm import tqdm
from pandas import ExcelWriter
import re
import json


SAVE_BY_ID = False # Сохраняет в бд по названию id, иначе по русскому названию
OUTPUT = 'csv' # json / xlsx / csv
FILE_NAME = 'data'
ONLY_ONE_CATEGORY = False # Собирать только с одной категории(watch)
TREE_DESCRIPTION = True
LINK = True
PARSE_PRODUCTS = None
MODE = 3
VISITED_PAGE = set()
start_url = 'https://parsinger.ru/html/index1_page_1.html'
NAMES = [
    ('title', 'Название'), 
    ('article', 'Артикул'), 
    ('price', 'Цена'), 
    ('old_price', 'Старая цена'), 
    ('in_stock', 'В наличии')]



def get_int(row):
    return int(re.sub(r'\D', '', row))

class RetryUrl(Exception):
    pass

class Parser:
    def __init__(self, start_url):
        self.error_urls = set()
        self.link_to_category = set()
        self.vistied_page = set()
        self.product_links = set()
        self.categories_links = set()
        self.pagination_links = set()
        self.counter = 0
        self.data = []
        self.main_url = 'https://parsinger.ru/html/'
        self.start_parsing(start_url)


    def start_parsing(self, start_url):
        self.parse_page(start_url)
        if not ONLY_ONE_CATEGORY:
            print(f'собрал {len(self.categories_links)} категорий')
            for link in tqdm(self.categories_links, desc='categories'):
                try:
                    self.parse_page(link)
                except RetryUrl:
                    self.counter += 1
        
        for link in tqdm(self.pagination_links, desc='Pagination'):
            try:
                self.parse_page(link)
            except RetryUrl:
                self.counter += 1
        
        for link in tqdm(list(self.product_links)[:PARSE_PRODUCTS], desc='Products'):
            self.parse_product_page(link)
        self.finish_spider()
    
    def get_request(self, url) -> Selector:
        '''Отправляет запрос, возвращает селектор, аналог soup из bs4
        '''
        if url not in VISITED_PAGE:
            try: 
                response = requests.get(url)
                response.encoding = 'utf-8'
                VISITED_PAGE.add(response.url)
                return Selector(response.text)
            except Exception as e:
                print(f'Не удалось получить ответ\n{url = }\n{e}')
                self.error_urls.add(url)
        else:
            raise RetryUrl('Уже проходил')


    def finish_spider(self):
        print(f'{self.counter} Пытался пройти по второму кругу')
        print(f'Общее количество пройденных страниц: {len(VISITED_PAGE)}')
        print(f'Общее количество собранных товаров: {len(self.data)}')
        if self.error_urls:
            print(f'URL который не удалось пройти: {self.error_urls} ')
        df = pd.DataFrame(self.data)

        if MODE == 1: 
            try:
                df = df[['title', 'Бренд', 'Материал корпуса', 'Тип экрана дисплея', 'Тип','price']]
            except KeyError:
                print('Спарсил еще не все столбцы')

        if not SAVE_BY_ID:
            for eng, rus in NAMES:
                df.rename(columns={eng:rus}, inplace=True)

        if MODE == 3:
            try: 
                df = df[['Название', 'Артикул', 'Бренд', 'Модель','В наличии','Цена','Старая цена', 'Ссылка']]
            except:
                print('Что то пошло не так с переименованием столбцов (def finish_spider)')


        if OUTPUT == 'json':
            file_name = f'{FILE_NAME}.json'
            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, indent=4, ensure_ascii=False, )

        if OUTPUT == 'xlsx':
            file_name = f'{FILE_NAME}.xlsx'
            with ExcelWriter(file_name) as writer:
                df.to_excel(writer, index=False)

        if OUTPUT == 'csv': 
            file_name = f'{FILE_NAME}.csv'
            df.to_csv(file_name, index=False)
        print(f'успешно сохранил файл {file_name}')

    def parse_page(self, url):
        selector = self.get_request(url)
        self.get_categories_link(selector)
        self.get_pagination_links(selector)
        self.get_products_links(selector)


    def get_categories_link(self, selector: Selector):
        for link in selector.xpath('//div[@class="nav_menu"]/a'):
            self.categories_links.add(self.main_url + link.xpath('.//@href').get())


    def get_pagination_links(self, selector: Selector):
        for link in selector.xpath('//div[@class="pagen"]/a/@href'):
            if link.get() not in self.pagination_links:
                self.pagination_links.add(self.main_url + link.get())


    def get_products_links(self, selector: Selector):
        links = selector.xpath('//div[@class="item_card"]//div[@class="sale_button"]/a/@href')
        for link in links:
            self.product_links.add(self.main_url + link.get())


    def parse_product_page(self, url):
        selector = self.get_request(url)
        product = {}
        try:
            product['title'] = selector.xpath('//p[@id="p_header"]/text()').get()
            product['article'] = selector.xpath('//p[@class="article"]/text()').get()
            if product.get('article'):
                product['article'] = int(product['article'].split(':')[1].strip())
            product['price'] = get_int(selector.xpath('//span[@id="price"]/text()').get())
            product['old_price'] = get_int(selector.xpath('//span[@id="old_price"]/text()').get())
            product['in_stock'] = get_int(selector.xpath('//span[@id="in_stock"]/text()').get())
            if LINK:
                product['Ссылка'] = url
            lst_li = selector.xpath('//ul[@id="description"]/li')
            if TREE_DESCRIPTION and OUTPUT=='json':
                product['description'] = {}
            for li in lst_li:
                try:
                    param, value = li.xpath('.//text()').get().split(':')
                except:
                    param, *value = li.xpath('.//text()').get().split(':')
                    value = list(map(str.strip, value))
                    value = ':'.join(value)
                if SAVE_BY_ID:
                    param = li.xpath('.//@id').get()
                if not TREE_DESCRIPTION or OUTPUT !='json': 
                    product[param.strip()] = value.strip()
                else:
                    product['description'][param.strip()] = value.strip()
            self.data.append(product)
        except Exception as e: 
            print(f'Не удалось распарсить\n{url = }\n{e}')


parser = Parser(start_url)