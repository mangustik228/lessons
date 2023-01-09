from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from tqdm import tqdm


url = 'https://parsinger.ru/infiniti_scroll_3/'


def get_result_one_column(page: Page, xpath):
    result = 0
    last_id = ''
    
    while True:
        el = page.locator(f'{xpath}[last()]')
        curr_id = el.get_attribute('id')
        el.click()
        if curr_id == last_id:
            break
        else:
            last_id = curr_id
        page.wait_for_timeout(900)

    values = page.query_selector_all(xpath)
    for value in values:
        result += int(value.inner_text())
    return result


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.wait_for_timeout(1200)
    result = 0
    for i in tqdm(range(1,6)):
        print(result)
        result += get_result_one_column(page, f'//div[@id="scroll-container_{i}"]/span')
    print(result)