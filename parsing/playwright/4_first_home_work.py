from playwright.sync_api import sync_playwright

url = 'https://parsinger.ru/selenium/1/1.html'

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator('//input[@name="first_name"]').fill('Vasiliy')
    page.locator('//input[@name="last_name"]').fill('Ovchinnikov')
    page.locator('//input[@name="patronymic"]').fill('Vasilievich')
    page.locator('//input[@name="age"]').fill('33')
    page.locator('//input[@name="city"]').fill('Samui')
    page.locator('//input[@name="email"]').fill('bacek.mangust@gmail.com')
    page.locator('//input[@type="button"]').click()
    page.wait_for_timeout(7000)
