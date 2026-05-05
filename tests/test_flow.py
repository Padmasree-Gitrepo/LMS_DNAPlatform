import inspect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage
from utils.config import BASE_URL, USERNAME, PASSWORD


def test_full_flow(page):

    # Login
    login = LoginPage(page)
    
    login.navigate(BASE_URL)
   
    login.click_sso()
    

    print("SSO URL:")

    # Fill username
    page.locator("input[id='signInFormUsername']:visible").fill(USERNAME)
   
    # Fill password
    page.locator("input[id='signInFormPassword']:visible").fill(PASSWORD) 
    page.wait_for_timeout(1000)
    
    #Login
    page.locator("input[name='signInSubmitButton']:visible").click()

   

    # Switch back to main page
    page.wait_for_load_state()
    page.wait_for_selector("text=Leave Summary")

    # ✅ 1.Successful login
    print("Current URL:", page.url)

    # ✅ 2. Validate login success and redirection
    assert "leaves" in page.url

    # ✅ 3. Validate Leave Summary heading
    assert login.verify_login_success()
    print("Login validation successful ✅")
    page.locator("button[class='onetrust-close-btn-handler banner-close-button ot-close-icon']").click()

    
    # Dashboard
    dashboard = DashboardPage(page)
    # 1. Validate 4 categories
    dashboard.validate_categories_count()

    # 2. Print categories
    dashboard.print_categories()

    # 3. Validate profile details
    profile = dashboard.get_profile_details()
    print("Profile:", profile)

    assert profile["email"] is not None
    assert profile["role"] is not None
    assert profile["empid"] is not None

    # 4. Validate side panel options
    dashboard.validate_sidepanel_options()
   
    # Apply Leave
    leave = LeavePage(page)
    leave.apply_leave()
    assert leave.verify_leave_applied()

    # Cancel Leave
    leave.cancel_leave()

    # Logout
    page.click(".profile-icon")
    page.click("text=Logout")

    assert page.locator("text=Login").is_visible()