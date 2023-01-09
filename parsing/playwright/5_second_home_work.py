from playwright.sync_api import sync_playwright

url = "https://parsinger.ru/selenium/2/2.html"

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.locator('xpath=//a[contains(text(), "16243162441624")]').click()
    res = page.locator('xpath=//p[@id="result"]')
    print(res.inner_text())