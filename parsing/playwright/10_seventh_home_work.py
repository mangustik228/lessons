from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/selenium/7/7.html'

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    # page.on('')
    page.goto(url)
    page.wait_for_timeout(1000)
    values = page.locator('xpath=//select/option')
    my_sum = 0
    for value in values.element_handles():
        my_sum += int(value.inner_text())
    page.wait_for_timeout(1000)
    print(my_sum)
    input_box = page.locator('xpath=//input[@type="text"]')
    input_box.fill(f'{my_sum}')
    input_box.press('Enter')
    page.wait_for_timeout(1000)
    page.locator('xpath=//input[@type="button"]').click()
    page.wait_for_timeout(22000)