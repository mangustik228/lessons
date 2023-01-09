from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

url = 'http://parsinger.ru/blank/0/'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    pages = []
    for i in range(1,7):
        page = context.new_page()
        page.goto(f'{url}{i}.html')
        pages.append(page)
        page.wait_for_timeout(50)
    for p in pages:
        print(p.title())    
    page.wait_for_timeout(100)    