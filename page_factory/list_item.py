import allure
from page_factory.component import Component


class ListItem(Component):
    @property
    def type_of(self) -> str:
        return 'list item'
            
    def choose(self, text: str, **kwargs) -> None:
        with allure.step(f'Typing into {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.select_option(value=text)
