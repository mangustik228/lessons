
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=%2FsearchSuggestions%2F%3Ftext%3D%26url%3D%2Fseller%2Fproffi-1%2Fproducts%2F%3Fminiapp%3Dseller_1%26text%3D%7Bvalue%7D')
    content = page.text_content('pre')
    page.wait_for_timeout(10000)
    browser.close()

print(content)