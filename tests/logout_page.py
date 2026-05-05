def test_logout(page):
    page.click(".profile-icon")
    page.click("text=Logout")

    assert page.locator("text=Login").is_visible()