from playwright.sync_api import sync_playwright, Playwright
import os

path_to_extension = "/home/bacek/.config/google-chrome/Profile 1/Extensions/bpflbjmbfccblbhlcmlgkajdpoiepmkd/1.4.1_0"
user_data_dir = f"{os.getcwd()}/tmp/test-user-data-dir"


def run(playwright: Playwright):
    context = playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        viewport={"width": 1600, "height": 800},
        args=[
            f"--disable-extensions-except={path_to_extension}",
            f"--load-extension={path_to_extension}",
        ],
    )
    page = context.new_page()
    page.goto('https://pioner.ru')
    page.wait_for_timeout(6000)
    print(page.title())
    page.close()
    # Test the background page as you would any other page.
    context.close()


with sync_playwright() as playwright:
    run(playwright)