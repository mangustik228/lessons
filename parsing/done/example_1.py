from bs4 import BeautifulSoup
import requests
import re
from tqdm import tqdm

def extract_titles(items):
    lst_titles = []
    for item in items:
        titles = item.find_all('a')
        title = titles[1].text
        lst_titles.append(title)
    return lst_titles

def get_int(txt:BeautifulSoup) -> int:
    txt = txt.text 
    digital = re.sub(r'\D', '', txt)
    return int(digital)

def get_soup(url:str) -> BeautifulSoup:
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup

def extract_links(items):
    url_pattern = 'https://parsinger.ru/html/'
    links = []
    for item in items:
        link = item.find_all('a')[0]['href']
        links.append(link)
    links = [url_pattern + link for link in links]
    return links

def parse_one_page(url):
    soup = get_soup(url)
    lst_items = soup.find_all('div', class_='item')
    titles = extract_titles(lst_items)
    links = extract_links(lst_items)
    return titles, links

def extract_article(url):
    soup = get_soup(url)
    art = soup.find('p', class_='article')
    art = get_int(art)
    return art

def extract_sum(url):
    soup = get_soup(url)
    stock = soup.find('span', id='in_stock')
    price = soup.find('span', id='price')
    stock = get_int(stock)
    price = get_int(price)
    return stock * price

if __name__ == '__main__':
    total_sums = []
    for i in range(1,6):
        for j in tqdm(range(1,5)):
            url = f'https://parsinger.ru/html/index{i}_page_{j}.html'
            titles, links = parse_one_page(url)
            for link in links: 
                total_sum = extract_sum(link)
                total_sums.append(total_sum)
    print(f'Сумма всех артиклей: {sum(total_sums)}')
