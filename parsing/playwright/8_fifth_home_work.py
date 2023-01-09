from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/selenium/4/4.html'

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    boxes = page.locator('xpath=//input[@class="check"]')
    for box in boxes.element_handles():
        box.click()
    page.locator('xpath=//input[@type="button"]').click()
    page.wait_for_timeout(10000)