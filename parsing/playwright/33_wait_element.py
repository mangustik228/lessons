from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/expectations/6/index.html'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.locator('//button').click()
    page.wait_for_selector('//*[@class="Y1DM2GR"]')
    value = page.locator('//*[@class="Y1DM2GR"]').inner_text()
    print(value)