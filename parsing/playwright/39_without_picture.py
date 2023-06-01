import asyncio
from playwright.async_api import async_playwright, BrowserContext

url = 'https://parsinger.ru/html/watch/1/1_1.html'
            
async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        # ---------------------------------- ВОТ ГЛАВНЫЙ КУСОК ----------------------------
        await page.route("**/*", lambda route: route.abort()
            if route.request.resource_type == "image"
            else route.continue_()
            )
        # ---------------------------------------------------------------------------------
        await page.goto(url)
        await page.wait_for_timeout(8000)
        print(await page.title())
        await page.close()
   
if __name__ == '__main__':
    asyncio.run(main())