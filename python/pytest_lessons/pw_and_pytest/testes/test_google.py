# from playwright.sync_api import Page
from playwright.async_api import Page


def test_hello_world(page: Page):
    url = "https://www.google.com/"
    page.goto(url)
    page_name = page.title()
    page.close()
    print(page_name)
    assert 1 == 1
    page.get
