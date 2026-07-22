from playwright.sync_api import Page, expect, Playwright

def test_playwrightBasic(playwright):
    browser=playwright.chromium.launch(headless=False)
    browser_context=browser.new_context()
    page=browser_context.new_page();
    page.goto("https://www.google.com/")


# if we  use page as fixture only get the defaul bwoeser as chrome and run in headless mode//
def test_playwrightBasic2(page:Page):
    page.goto("https://www.crazygames.com/")
    page.pause()

def test_corelocator(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK")
    page.get_by_role("combobox").select_option("Student")
    page.get_by_role("link",name="terms and conditions").click()
    page.locator("#signInBtn").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_fireFoxFlow(playwright: Playwright):
    firefoxBrowser=playwright.firefox.launch(headless=False)
    fireFoxContext=firefoxBrowser.new_context()
    page=fireFoxContext.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")


