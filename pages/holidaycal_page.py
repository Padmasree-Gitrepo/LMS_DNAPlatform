from playwright.sync_api import Page, expect

class HolidayPage:

    def __init__(self, page: Page):
        self.page = page

    # 🔹 Navigate to Holiday Calendar
    def go_to_holiday_calendar(self):
        menu = self.page.locator("li[role='menuitem']").nth(2) # adjust index if needed
        expect(menu).to_be_visible()
        menu.click()

        expect(self.page.locator("text=Holiday Calendar")).to_be_visible()

    # 🔹 Print months + holidays
    def print_holidays(self):

        self.page.wait_for_selector("[data-testid='month-card']")
        months = self.page.locator("[data-testid='month-card']").all()

        print("Month count:", len(months))

        for month in months:
        # Get text
            text = month.inner_text()
            lines = [l.strip() for l in text.split("\n") if l.strip()]

            if len(lines) > 0:

            # Month name
                month_name = lines[0]
                print(f"\n📅 {month_name}")

                j = 1
                while j < len(lines) - 1:

                    date = lines[j]
                    name = lines[j + 1]

                    if "/" in date:
                        print(f" - {date} : {name}")
                        j += 2
                    else:
                        j += 1