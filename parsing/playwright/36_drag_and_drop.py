from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/draganddrop/3/index.html'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    block = page.locator('xpath=//div[@id="block1"]')
    for i in range(1,6):
        block.drag_to(page.locator(f'xpath=//div[@id="point{i}"]'))
        page.wait_for_timeout(500)
        block = page.locator('xpath=//div[@id="block1"]')
    page.wait_for_timeout(5000)
    print(page.inner_text('xpath=//p[@id="message"]'))
