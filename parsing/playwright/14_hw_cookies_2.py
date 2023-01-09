from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/methods/5/index.html'
base_url = 'https://parsinger.ru/methods/5/'

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    current_value = 0
    max_cookie = 0
    page = context.new_page()
    page.goto(url)
    links = page.locator('xpath=//div[@class="urls"]/a')
    urls = []
    for link in links.element_handles():
        urls.append(link.get_attribute('href'))
    
    for url in urls: 
        page.goto(base_url + url)
        cookie = context.cookies()[0].get('expires')
        if max_cookie < int(cookie):
            max_cookie = int(cookie)
            current_value = page.locator('xpath=//p[@id="result"]').inner_text()
        print(current_value)

