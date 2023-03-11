from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/draganddrop/2/index.html'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    drag = page.locator('xpath=//div[@id="draggable"]')
    for i in range(1,5):
        drag.drag_to(page.locator(f'xpath=//div[@id="box{i}"]'))
        page.wait_for_timeout(1000)
    print(page.inner_text('xpath=//div[@id="result"]'))
    page.wait_for_timeout(1000)
    print(f'{page.title() = }')