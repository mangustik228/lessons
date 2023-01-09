from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/infiniti_scroll_1/'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    page.locator('(//input)[1]').press('Enter')
    result, last_span, visited_spans = [], None, []
    page.wait_for_timeout(1500)
    while True:
        for i in range(500):
            page.locator('(//div[@id="scroll-container"]/span)[last()]').press('Tab')
            page.keyboard.press('ArrowDown')
        page.wait_for_timeout(1500)
        spans = page.query_selector_all('//div[@id="scroll-container"]/span')
        if last_span == spans[-1].get_attribute('id'):
            break
        for span in spans: 
            last_span = spans[-1].get_attribute('id')
            id_span = span.get_attribute('id')
            if id_span not in visited_spans:
                visited_spans.append(id_span)
                value = int(span.inner_text())
                result.append(value)
                print(value)
        print(f'{sum(result)}')
        print(f'{len(result)}')