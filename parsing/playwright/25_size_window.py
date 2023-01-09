from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/window_size/1/'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={'width':1200,'height':600})
    page = context.new_page()
    page.wait_for_timeout(1500)
    page.goto(url)
    page.wait_for_timeout(1500)
    height = page.evaluate('window.innerHeight')
    width = page.evaluate('window.innerWidth')
    page.set_viewport_size({'width':555, 'height':555})
    page.wait_for_timeout(1500)
    print(f'{height = } | {width = }')
    # print(page.evaluate('window.innerWidth'))
    page.wait_for_timeout(4000)
    print(page.locator('//span[@id="result"]').inner_text())