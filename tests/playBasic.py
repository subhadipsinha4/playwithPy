from playwright.sync_api import Page

def test_playwrightBasic(playwright):
    browser=playwright.chromium.launch(headless=False)
    browser_context=browser.new_context()
    page=browser_context.new_page();
    page.goto("https://www.google.com/")


# if we  use page as fixture only get the defaul bwoeser as chrome and run in headless mode//
def test_playwrightBasic2(page:Page):
    page.goto("https://www.crazygames.com/")
    page.pause()
