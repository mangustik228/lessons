from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/blank/modal/2/index.html'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.on("dialog", lambda dialog: dialog.accept())
    buttons = page.locator('//input')
    for button in buttons.element_handles():
        button.click()
        result = page.locator('//p[@id="result"]')
        result = result.inner_text()
        if result:
            print(result)
    page.wait_for_timeout(5000)
    browser.close()
