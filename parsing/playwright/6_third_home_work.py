from playwright.sync_api import sync_playwright

url = "https://parsinger.ru/selenium/3/3.html"

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    values = page.locator('xpath=//p')
    data = []
    for value in values.element_handles():
        data.append(int(value.inner_text().strip()))
    print(sum(data))