from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/scroll/1/'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    buttons = page.locator('xpath=(//div[@class = "item"]/input)')
    for button in buttons.element_handles():
        button.press('Tab')
        button.press('Space')
    print(f'{page.title() = }')


