import pytest
from playwright.sync_api import Page, sync_playwright
from pages.calendar_constructor import CalendarConstructor
from settings import BASE_URL


@pytest.fixture(scope='class', autouse=True)
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        page = chromium.new_page()
        yield page
        #page.pause()

@pytest.fixture(scope='class', autouse=True)
def test_cal_const(chromium_page: Page) -> CalendarConstructor:
    page_to_test = CalendarConstructor(chromium_page)
    page_to_test.visit(BASE_URL)
    yield page_to_test

@pytest.fixture(scope='function', autouse=True)
def test_cal_single(chromium_page: Page, test_cal_const: CalendarConstructor) -> None:
    yield
    test_cal_const.cal_form.flush_form()
    #chromium_page.pause()
    
