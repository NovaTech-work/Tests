from pages import TheInternet
from playwright.sync_api import Page
from locators import *


def test_checkbox(page:Page):
    internet = TheInternet(page)
    internet.openCheckbox(url)
    page.locator(checkbox).click()
    page.locator(checkbox2).click()


