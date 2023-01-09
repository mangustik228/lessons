from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/scroll/3/'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    inputs = page.locator('xpath=//div[@class="item"]/input')
    result = 0
    for input in inputs.element_handles():
        input.click()
        page.wait_for_timeout(50)
        flag = input.query_selector('..//span[contains(@id, result)]').inner_text()
        if flag:
            value = input.get_attribute('id')
            print(value)
            result += int(value) 
    print(result)