from playwright.sync_api import sync_playwright
from tqdm import tqdm

url = 'https://parsinger.ru/window_size/2/index.html'
window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]


with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    page.wait_for_timeout(500)
    for x in tqdm(window_size_x):
        for y in window_size_y:
            page.set_viewport_size({'width':x,'height':y})
            page.wait_for_timeout(100)
            value = page.locator('//*[@id="result"]').inner_html()
            h = page.evaluate('window.innerHeight')
            w = page.evaluate('window.innerWidth')
            if value:
                data = {}
                data['width'] = x
                data['height'] = y
                print(data)