class LogoutPage:
    def __init__(self,page):
        self.page = page
        
    def click_profile(self):
        self.page.click(".user-profile-trigger-name")
        self.page.click("text=Logout")
        # wait for page to load
        self.page.wait_for_load_state("networkidle")

    # wait for login element
        self.page.wait_for_selector("text=Login", timeout=10000)
        assert self.page.locator("text=Login using SSO").is_visible()