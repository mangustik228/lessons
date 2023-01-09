# https://playwright.dev/python/docs/dialogs

from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

url = 'https://parsinger.ru/blank/modal/3/index.html'

PINS = []

def write_pin(dialog, page: Page):
    txt = dialog.message
    dialog.dismiss()
    page.locator('//input[@type="text"]').fill(txt)
    page.locator('//input[@id="check"]').click()



with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.on('dialog', lambda dialog: write_pin(dialog, page))
    inputs = page.locator('//input[@class="buttons"]')
    result = ''
    for input in inputs.element_handles():
        input.click()
        page.wait_for_timeout(50)
        value = page.locator('//p[@id="result"]').inner_text()
        if value != result:
            print(value)
            result = value
    page.wait_for_timeout(2000)
    page.close()