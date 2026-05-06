from playwright.sync_api import expect

class WfhPage:

    def __init__(self, page):
        self.page = page

    def apply_wfh(self, reason_type, start_date, end_date, notes):

        # 1. Open WFH section
        self.page.click("text=Apply Work from Home")
        self.page.wait_for_selector("text=Apply Work from Home")

        # 2. Reason Type
        self.page.locator(".ant-select-selector").first.click()
        self.page.locator(".ant-select-item-option",
                          has_text=reason_type).first.click()

        # 3. START DATE
        start_input = self.page.locator(".ant-picker-input input").nth(0)
        start_input.click()

        start_calendar = self.page.locator(".ant-picker-dropdown:visible")
        expect(start_calendar).to_be_visible()

        start_date_cell = start_calendar.locator(
            ".ant-picker-cell-in-view:not(.ant-picker-cell-disabled) .ant-picker-cell-inner",
            has_text=str(start_date)
        ).first

        expect(start_date_cell).to_be_visible()
        start_date_cell.click()

        self.page.wait_for_timeout(300)

        # 4. END DATE
        end_input = self.page.locator(".ant-picker-input input").nth(1)
        expect(end_input).to_be_enabled()
        end_input.click()

        end_calendar = self.page.locator(".ant-picker-dropdown:visible")
        expect(end_calendar).to_be_visible()

        end_date_cell = end_calendar.locator(
            ".ant-picker-cell-in-view:not(.ant-picker-cell-disabled) .ant-picker-cell-inner",
            has_text=str(end_date)
        ).first

        expect(end_date_cell).to_be_visible()
        end_date_cell.click()

        self.page.wait_for_timeout(300)

        # 5. NOTES
        notes_box = self.page.locator("textarea")
        expect(notes_box).to_be_visible(timeout=10000)
        notes_box.fill(notes)

        # 6. APPLY BUTTON
        apply_btn = self.page.locator("button:has-text('Apply')").last
        expect(apply_btn).to_be_visible()
        expect(apply_btn).to_be_enabled()
        apply_btn.click()

    # 7. VERIFY METHOD 
    
    def verify_wfh_applied(self):
        success_msg = self.page.locator("text=Work From Home Request Sent")
        expect(success_msg).to_be_visible(timeout=10000)
        return success_msg.is_visible()
    
    

    
    # Cancel leave
    # 🔹 Navigate to Leave & Absence Tracker
    def go_to_leave_tracker(self):
        menu_item = self.page.locator("li[role='menuitem']").nth(1)
        expect(menu_item).to_be_visible()
        menu_item.click()

    # 🔹 Open filter panel
    def open_filters(self):
        self.page.get_by_label("Open filters").click()

    # 🔹 Apply Leaves filter
    def apply_leaves_filter(self):
        filter_panel=self.page.locator("[role='dialog']")
        filter_panel.get_by_role("button",name="Request Type").click()
        filter_panel.get_by_role("checkbox", name="Work from Home").check()
        filter_panel.get_by_role("button", name="Apply").click()

    # 🔹 Cancel WFH request
    def cancel_wfh(self):
        section = self.page.get_by_text("My Scheduled Absences")
        expect(section).to_be_visible(timeout=15000)

        rows = self.page.locator("tr", has_text="Work From Home")

        if rows.count() == 0:
            raise Exception("❌ No WFH request found to cancel")

        row = rows.first
        cancel_btn = row.get_by_role("button", name="Cancel")

        expect(cancel_btn).to_be_visible()
        cancel_btn.click()

        # Handle confirmation popup
        confirm = self.page.locator("button:has-text('Yes'), button:has-text('Confirm')")
        if confirm.is_visible():
            confirm.click()

    # 🔹 Verify success message
    def verify_cancel_success(self):
        success = self.page.locator(
            "text=Work From Home cancelled successfully"
        )
        expect(success).to_be_visible(timeout=10000)
        return success.is_visible()