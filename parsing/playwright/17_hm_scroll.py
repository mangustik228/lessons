from playwright.sync_api import sync_playwright
from random import randint

url = 'https://parsinger.ru/scroll/2/index.html'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    result = 0
    elements = page.locator('//div[@class="item"]/input')
    for element in elements.element_handles():
        element.click()
        value = element\
            .query_selector('xpath=..//span[contains(@id, "result")]')\
            .inner_text()
        try:
            result += int(value)
        except ValueError:
            pass
    print(result)
