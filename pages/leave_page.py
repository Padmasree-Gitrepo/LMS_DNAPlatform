class LeavePage:

    def __init__(self, page):
        self.page = page

    def apply_leave(self):
        self.page.click("text=Apply Leave")
        self.page.fill("#fromDate", "2026-05-10")
        self.page.fill("#toDate", "2026-05-11")
        self.page.fill("#reason", "Medical leave")
        self.page.click("text=Submit")

    def verify_leave_applied(self):
        return self.page.locator("text=Leave Applied Successfully").is_visible()

    def cancel_leave(self):
        self.page.click("text=Leave Tracker")
        self.page.click("text=Filter")
        self.page.click("text=Leaves")
        self.page.click("text=Cancel")