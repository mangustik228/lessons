import asyncio
from playwright.async_api import async_playwright

url = 'https://google.com'

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        print(f'{await page.title() = }')

if __name__ == '__main__':
    asyncio.run(main())