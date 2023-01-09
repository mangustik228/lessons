from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/expectations/4/index.html'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.locator('//button').click()
    while True:
        if 'JK8HQ' in page.title():
            print(page.title())
            break