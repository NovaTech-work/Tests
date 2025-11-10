import re
from playwright.sync_api import Page, expect
from .base import BasePage

class TheInternet(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def openCheckbox(self,url):
        super().open(url)
        self.page.get_by_role("link", name="Checkboxes").click()

