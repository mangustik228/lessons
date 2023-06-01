from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/draganddrop/3/index.html'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    element = page.locator('xpath=//div[@id="block1"]')
    box = element.bounding_box()
    page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2 + 5)
    page.mouse.down()
    page.mouse.move(box["x"] + box["width"] + 600 / 2, box["y"] + box["height"] / 2 + 5, steps=50)
    page.mouse.up()
    page.wait_for_timeout(5000)