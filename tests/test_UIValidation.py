from playwright.sync_api import Page

def test_UIAfterLogin(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("Student")
    page.get_by_role("link",name="terms and conditions").click()
    page.locator("#signInBtn").click()

    product1=page.locator("app-card").filter(has_text="Nokia Edge")
    product1.get_by_role("button",name="Add").click()

