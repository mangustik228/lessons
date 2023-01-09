from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/expectations/3/index.html'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.locator('//button').click()
    page.wait_for_timeout(15000)
    while True:
        if page.title() == '345FDG3245SFD':
            print(page.locator('//*[@id="result"]').text_content())
            break
