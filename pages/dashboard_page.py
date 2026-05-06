class DashboardPage:

    def __init__(self, page):
        self.page = page

    #  Get all leave categories
    def get_leave_categories(self):
        return self.page.locator(".legend-label")

    #  Validate 4 categories
    def validate_categories_count(self):
        count = self.get_leave_categories().count()
        print(count)
        assert count == 4, f"Expected 4 categories, but got {count}"

    #  Print categories + count
    def print_categories(self):
        labels = self.page.locator(".legend-label").all_text_contents()
        values = self.page.locator(".legend-value").all_text_contents()

        for l, v in zip(labels, values):
            print(f"{l}: {v}")
    

    #  Profile validation
    def get_profile_details(self):
        self.page.locator(".user-profile-trigger-name").click()

        return {
            "email": self.page.locator("text=@").text_content(),
            "role": self.page.locator("text=Engineer").text_content(),
            "empid": self.page.locator("text=Emp Id").text_content()
        }

    #  Side panel options count
    def validate_sidepanel_options(self):
        options = self.page.locator("ul.ant-menu li.ant-menu-item")
        count =options.count()
        print(count)
        texts= options.all_text_contents()
        print(texts)
        count = options.count()
        assert count == 3, f"Expected 4 side pane options, got {count}"