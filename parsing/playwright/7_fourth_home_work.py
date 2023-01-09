from playwright.sync_api import sync_playwright
from parsel import Selector

url = "https://parsinger.ru/selenium/3/3.html"

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    selector = Selector(page.content())
    data = []
    values = selector.xpath('//div[@class="text"]/p[2]/text()')
    for value in values:
        data.append(int(value.get()))
    print(sum(data))