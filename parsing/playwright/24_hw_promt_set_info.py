from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, Dialog

url = 'https://parsinger.ru/blank/modal/4/index.html'


def read_info(page: Dialog):
    page.accept(txt)

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.on('dialog', read_info)
    pins = page.locator('//span[@class="pin"]')
    for pin in pins.element_handles():
        txt = pin.inner_text()
        page.locator('//input[@value="Проверить"]').click()
        print(f'{txt = }  |', page.locator('//p[@id="result"]').inner_text())