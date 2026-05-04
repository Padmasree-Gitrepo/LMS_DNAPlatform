from utils.config import BASE_URL
class LoginPage:
 def __init__(self, page):
    self.page = page
def navigate(self):
     self.page.goto(BASE_URL)
 def click_sso_login(self):
    self.page.click("text=Login using SSO")
 def login(self, username, password):
    self.page.fill("input[name='username']", username)
 self.page.fill("input[name='password']", password)
 self.page.click("button[type='submit']")
def validate_login_success(self):
    return self.page.locator("text=Leave Summary").is_visible()