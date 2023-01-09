from playwright.sync_api import sync_playwright
from pprint import pprint
import re
url = 'https://parsinger.ru/methods/3/index.html'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    cookies = context.cookies()
    sum_cookies = 0
    for cookie in cookies:
        number = re.sub(r'\D', '', cookie.get('name'))
        if not int(number) % 2:
            sum_cookies += int(cookie.get('value'))
    pprint(cookies)
    print(f'{sum_cookies}')