from playwright.sync_api import Page
from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.button import Button
from page_factory.title import Title


class CalendarForm:
    def __init__(self, page: Page) -> None:
        self.page = page
        
        # Поле Выбрать тематику
        self.subject_list = ListItem(
            page, locator="{custom}", name='Список Выбрать тематику'
        )
        
        # Очистить всю тематику
        self.subject_flush = Button(
            page, locator=".checkselect[data-select='Выбрать тематику'] ~ .checkselect-clear", name='Кнопка Очистить тематику'
        )
        
        # Поле Все страны
        self.country_list = ListItem(
            page, locator="{custom}", name='Поле Все страны'
        )
        
        # Очистить все страны
        self.country_flush = Button(
            page, locator=".checkselect[data-select='Все страны'] ~ .checkselect-clear", name='Кнопка Очистить страны'
        )

        # Поле Ширина  
        self.width_input = Input(
            page, locator="[name='width']", name='Поле Ширина'
        )
        
        # Поле Высота  
        self.height_input = Input(
            page, locator="[name='height']", name='Поле высота'
        )
        
        # Синяя кнопка
        self.radio_blue = Button(
            page, locator="input[value='blue'] ~ .radio__square", name='Кнопка синий'
        )
        
        # На всю ширину
        self.radio_width = Button(
            page, locator="input[name='full-width'] ~ .radio__square", name='Кнопка на всю ширину'
        )
        
        # На всю высоту
        self.radio_height = Button(
            page, locator="input[name='auto-height'] ~ .radio__square", name='Кнопка на всю высоту'
        )
        
        # Кнопка Сгенерировать
        self.generate = Button(
            page, locator="button:has-text('Сгенерировать превью')", name='Кнопка сгенерировать'
        )
        
        # Сгенерированный календарь
        self.calendar = Title(
            page, locator="div.events_wrap_table", name='Календарь'
        )
        
        
    def choose_subject(self, option: str):
        self.subject_list.click(custom=".checkselect[data-select='Выбрать тематику']")
        self.subject_list.click(custom=f".checkselect[data-select='Выбрать тематику'] span:has-text('{option}')")
        self.subject_list.click(custom=".checkselect[data-select='Выбрать тематику'] .checkselect-over")
        
    def choose_country(self, option: str):
        self.country_list.click(custom=".checkselect[data-select='Все страны']")
        self.country_list.click(custom=f".checkselect[data-select='Все страны'] span:has-text('{option}')")
        self.country_list.click(custom=".checkselect[data-select='Все страны'] .checkselect-over")
        
    def flush_form(self):
        self.subject_flush.click()
        self.country_flush.click()
            
        
