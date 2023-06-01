import asyncio
from playwright.async_api import async_playwright, BrowserContext

url = 'https://parsinger.ru/html/watch/1/1_'

lst = [i for i in range(1,20)]

async def parse_page(context: BrowserContext, i:int):
    page = await context.new_page()
    await page.goto(f'{url}{i}.html')
    await page.wait_for_timeout(8000)
    print(await page.title())
    await page.close()


async def gen_tasks(context: BrowserContext, i:int):
    while True: 
        if len(context.pages) > 5:
            await asyncio.sleep(0.1)
        else: 
            task = asyncio.ensure_future(parse_page(context, i))
            return task
            
async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        context = await browser.new_context()
        tasks = []
        for i in range(1, 20):
            task = await gen_tasks(context, i)
            tasks.append(task)
            if i >= 5:
                await tasks.pop(0)
        for i in tasks:
            await i
   
if __name__ == '__main__':
    asyncio.run(main())