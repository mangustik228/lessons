from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/methods/1/index.html'
flag = True

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()
    count = 0
    while True:
        page.goto(url)
        page.wait_for_timeout(500)
        if flag: 
            flag = False
            content = page.content()
        if page.content() != content:
            print(page.content())
            break
        else: 
            count += 1 
            print(count)
            page.reload()