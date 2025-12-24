import allure
from playwright.sync_api import Page, Response

from components.calendar.cal_form import CalendarForm


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cal_form = CalendarForm(page)

    def visit(self, url: str) -> Response | None:
        with allure.step(f'Opening the url "{url}"'):
            return self.page.goto(url, wait_until='networkidle')

    def reload(self) -> Response | None:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            return self.page.reload(wait_until='domcontentloaded')
