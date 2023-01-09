from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

url = 'https://parsinger.ru/scroll/4/index.html'

def get_number(page: Page):
    value = page.locator('//p[@id="result"]').inner_text()
    return int(value)

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.wait_for_timeout(1000)
    buttons = page.locator('xpath=//div[@class="visibility"]/button')
    result = 0
    for i in range(0, 50, 5):
        for button in buttons.element_handles()[i:i+5]:
            button.click()
            result += get_number(page)
            page.wait_for_timeout(300)
    print(result)