from playwright.sync_api import sync_playwright

url = 'https://v-project.ru/'


with sync_playwright() as pw:
    browser = pw.webkit.launch(headless=False)
    context = browser.new_context(
        user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1'
        # viewport={'width':799, 'height': 500}
    )
    page = context.new_page()
    page.goto(url)
