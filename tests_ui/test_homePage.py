from playwright.sync_api import Playwright
from pom.home_page import HomePage

def about_test(playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    home_page = HomePage(page)
    page.screenshot(path="../demo.png")
    browser.close()
