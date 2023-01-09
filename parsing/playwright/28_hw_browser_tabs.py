from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/blank/3/index.html'


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    m_page = context.new_page()
    m_page.goto(url)
    links = m_page.locator('//div[@class="main"]/input')
    for link in links.element_handles():
        link.click()
        m_page.wait_for_timeout(1000)
    result = 0
    for page in context.pages:
        try:
            result += int(page.title())
        except:
            pass
    print(result)