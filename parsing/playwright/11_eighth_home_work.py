from playwright.sync_api import sync_playwright
import re
url = 'https://parsinger.ru/selenium/6/6.html'

def calc(expresion:str):
    operation = {
        '*': lambda a,b: a * b,
        '+': lambda a,b: a + b,
        '-': lambda a,b: a - b,
        '/': lambda a,b: a / b,
    }
    expresion = expresion.replace('(','').replace(')','')
    for operator, func in operation.items():
        if operator in expresion:
            expresion = expresion.split(operator)
            return str(func(int(expresion[0]), int(expresion[1])))
     
def open_scobs(expresion):
    expresion = expresion.replace(' ', '')
    pattern = r'(\(\d*.\d*\))'
    try:
        result = re.findall(pattern, expresion)[0]
        new_value = calc(result)
        expresion = expresion.replace(result, new_value)
        return open_scobs(expresion)
    except Exception as e:
        return calc(expresion)


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    expresion = page.locator('xpath=//div[@id="text_box"]')
    expresion = expresion.text_content()
    result = open_scobs(expresion)
    page.locator('xpath=//select').click()
    page.wait_for_timeout(1000)
    print('раскрыл')
    value = page.locator(f'xpath=//option[contains(text(),"{result}")]').get_attribute('value')
    print('value')
    page.select_option('xpath=//select',value=value)
    # print('выбрал')
    # page.click(f'xpath=//option[contains(text(),"{result}")]')
    # print('кликнул')
    # page.press('Enter')
    # print('кнопка')
    page.wait_for_timeout(1000)
    page.locator('xpath=//input[@type="button"]').click()
    print('жахнул')
    page.wait_for_timeout(10000)

