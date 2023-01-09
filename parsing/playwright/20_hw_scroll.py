from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/infiniti_scroll_2/'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.wait_for_timeout(1000)
    last_el = ''
    while True:
        el = page.locator('//div[@id="scroll-container"]/p[last()]')
        current_id = el.get_attribute('id')
        el.click()
        page.wait_for_timeout(1500)
        print(f'{last_el = }  | {current_id = }')
        if last_el == current_id:
            break 
        else:
            last_el = current_id
    values = page.query_selector_all('//div[@id="scroll-container"]/p')
    res = 0
    for value in values:
        res += int(value.inner_text())
    print(res)
