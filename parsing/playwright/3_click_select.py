from playwright.sync_api import sync_playwright


url = 'https://parsinger.ru/html/watch/1/1_1.html'

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    model = page.locator('xpath=//li[@id="model"]')
    page.wait_for_timeout(1000)
    print(model)
    print(model.inner_text())
    page.wait_for_timeout(1000)
    page.locator('xpath=//button').click()
    print('По идеи кликнул')
    page.wait_for_timeout(1000)
    page.locator('xpath=//div[@class="back"]').click()
    page.wait_for_timeout(3000)
