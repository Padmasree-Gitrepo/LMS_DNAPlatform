from playwright.sync_api import expect
import re

class LeavePage:

    def __init__(self, page):
        self.page = page

    def apply_leave(self, leave_type, start_date, end_date, reason):

        self.page.click("text=Apply Leave")
        self.page.wait_for_selector("text=Apply Leave")

        # 1. Leave type
        self.page.locator(".ant-select-selector").first.click()
        self.page.locator(".ant-select-item-option",
                          has_text=leave_type).first.click()
       
        # 3. START DATE (datepicker)
        
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

        # 4. END DATE (datepicker)
       
        end_input = self.page.locator(".ant-picker-input input").nth(1)

        # wait until enabled (VERY IMPORTANT FIX)
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

       
        # 4. Reason
    
        reason_box = self.page.locator("textarea")
        expect(reason_box).to_be_visible(timeout=10000)
        reason_box.scroll_into_view_if_needed()
        reason_box.fill(reason)

        # 5. Submit
        apply_btn = self.page.locator("button:has-text('Apply')").last 
        apply_btn.wait_for(state="visible", timeout=10000) 
        expect(apply_btn).to_be_enabled() 
        apply_btn.scroll_into_view_if_needed() 
        apply_btn.click()

        #6.Verify leave applied successfully
        
        def verify_leave_applied(self):
            success_msg = self.page.locator("text=Leave Applied Successfully")
            expect(success_msg).to_be_visible(timeout=10000)
            return success_msg.is_visible()