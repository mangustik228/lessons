from playwright.sync_api import sync_playwright
from playwright.sync_api import BrowserContext
import numpy as np
from tqdm import tqdm


urls = [
    'http://parsinger.ru/blank/1/1.html', 
    'http://parsinger.ru/blank/1/2.html', 
    'http://parsinger.ru/blank/1/3.html',
    'http://parsinger.ru/blank/1/4.html', 
    'http://parsinger.ru/blank/1/5.html', 
    'http://parsinger.ru/blank/1/6.html',
]

def get_number(context: BrowserContext, url):
    page = context.new_page()
    page.goto(url)
    page.wait_for_timeout(100)
    page.locator('//input[@type="checkbox"]').click()
    value = page.locator('//*[@id="result"]').inner_text()
    value = int(value)
    page.close()
    return np.sqrt(value)



with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    data = []
    for url in tqdm(urls):
        data.append(get_number(context, url))
    sum_values = sum(data)
    print(np.round(sum_values, decimals=9))
