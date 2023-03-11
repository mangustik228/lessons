from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/draganddrop/1/index.html'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    drag = page.locator('xpath=//div[@id="draggable"]')
    field2 = page.locator('xpath=//div[@id="field2"]')
    drag.drag_to(field2)
    page.wait_for_timeout(3000)
    print(page.inner_text('xpath=//div[@id="result"]'))