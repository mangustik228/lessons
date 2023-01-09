import requests
from bs4 import BeautifulSoup
import csv


with open('lesson48_2.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром'])

goods  = ['watch', 'mobile', 'mouse', 'hdd', 'headphones']

for j in range(1, 6):
    for i in range(1, 33):
        url = f'https://parsinger.ru/html/{goods[j-1]}/{j}/{j}_{i}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = [i.text for i in soup.find_all('p', id="p_header")]
        articl  = [i.text.split(':')[1].strip() for i in soup.find_all('p', class_ = 'article')]
        brand = [i.text.split(':')[1].strip() for i in soup.find_all('li', id = 'brand')]
        model = [i.text.split(':')[1].strip() for i in soup.find_all('li', id = 'model')]
        nalichae = [i.text.split(':')[1].strip() for i in soup.find_all('span', id = 'in_stock')]
        price = [i.text for i in soup.find_all('span', id = 'price')]
        old_price = [i.text for i in soup.find_all('span', id='old_price')]



        for item, artic, brand_, model_,  nal,  price, op  in zip(name, articl, brand, model, nalichae, price, old_price):
            flatten = item, artic, brand, model, nal, price, op, url

            file = open('lesson48_2.csv', 'a', encoding='utf-8-sig', newline='')
            writer = csv.writer(file, delimiter=';')
            writer.writerow(flatten)
file.close()


