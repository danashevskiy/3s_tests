import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from pages.calendar_constructor import CalendarConstructor
from settings import BASE_URL


@pytest.fixture(scope='class', autouse=True)
def browser_page(browser: Browser) -> Page:
    with browser.new_context() as context, context.new_page() as page:
        yield page
        #page.pause() 

@pytest.fixture(scope='class', autouse=True)
def test_cal_const(browser_page) -> CalendarConstructor:
    page_to_test = CalendarConstructor(browser_page)
    page_to_test.visit(BASE_URL)
    yield page_to_test

@pytest.fixture(scope='function', autouse=True)
def test_cal_single(browser_page, test_cal_const: CalendarConstructor) -> None:
    yield
    test_cal_const.cal_form.flush_form()
    #browser_page.pause()
    
