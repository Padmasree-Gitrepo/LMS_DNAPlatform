class HolidayPage:

    def __init__(self, page):
        self.page = page

    def print_holidays(self):
        months = self.page.locator(".month").all_text_contents()
        holidays = self.page.locator(".holiday").all_text_contents()

        for m, h in zip(months, holidays):
            print(f"{m}: {h}")