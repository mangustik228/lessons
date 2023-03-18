from time import sleep
from loguru import logger
import requests
from configparser import ConfigParser
from parsel import Selector
from playwright.sync_api import sync_playwright
from playwright.sync_api._generated import Page
import base64


url = 'https://stepik.org/lesson/801947/step/1?unit=804922'

config = ConfigParser()
config.read('config.ini')
SOLVE_URL = config.get('CaptchaAI', 'solve_url')
KEY = config.get('CaptchaAI', 'key')
RESULT_URL = config.get('CaptchaAI', "result_url")
url = "https://captcha-parsinger.ru/?page=3"


def solve_captcha(image: bytes):
    data = {
        "key":KEY,
        "method":"post",
        "json":1,
        "min_len":4,
        "max_len":6,
        "language":2,
        "regsense":1
    }
    param = {
        "key":KEY,
        "action":"get",
        "json":1
    }
    files = {"file":image}
    
    response = requests.post(SOLVE_URL, data=data,files=files)
    logger.info(f'Послал запрос на решение: {response.json()}')
    param["id"] = response.json().get('request')
    logger.info(f"{param.get('id') = }")
    logger.info(param)
    sleep(8)
    request_json = requests.get(RESULT_URL, params=param).json()
    logger.info(f'{request_json}')
    return request_json.get('request')

def get_sum(page: Page):
    result = 0
    sel = Selector(page.content())
    prices = sel.xpath('//ul/li[1]/text()')
    for price in prices:
        price = price.get().split(':')[-1].strip()
        logger.info(f'{price = }')
        price.isdigit()
        result += int(price)
    return result

def check_page(page: Page):
    sel = Selector(page.content())
    return not sel.xpath('//div[@id="captcha"]')



with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    page.goto(url)
    while True:
        context.clear_cookies()
        page.reload()
        while True:
            page.wait_for_timeout(1000)
            captcha_box = page.locator('xpath=//div[@class="chakra-form-control css-1sx6owr"]/img')
            image = captcha_box.screenshot()
            result = solve_captcha(image)
            page.wait_for_timeout(1000)
            page.locator('xpath=//input[@id="field-:r0:"]').fill(result)
            page.wait_for_timeout(1000)
            page.click('xpath=(//button[@type="button"])[last()]')
            page.wait_for_timeout(1000)
            if check_page(page):
                break
        logger.info(get_sum(page))