class LoginPage:
    def __init__(self,page):
        self.page = page
    def navigate(self,url):
        self.page.goto(url) 
    def click_sso(self):
        self.page.click("text=Login using SSO")
    def verify_login_success(self):
        return self.page.locator("text=Leave Summary").is_visible()  
            
