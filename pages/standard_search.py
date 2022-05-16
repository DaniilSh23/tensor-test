from .base_search import BaseSearch
from .locators import StandardSearchLocators


class StandardSearch(BaseSearch):
    '''Класс для стандартного поиска Яндекса'''

    def should_be_search_box(self) -> None:
        '''
        Метод для проверки наличия поля для поиска.
        :return: None
        '''
        assert self.is_element_present(*StandardSearchLocators.SEARCH_FIELD), 'Search field not found.'

    def input_and_check_suggest(self, text: str) -> None:
        '''
        Метод для проверки наличия таблицы с подсказками
        :param text: str - текст, вводимый в поле для поиска
        :return: None
        '''
        text_area = self.browser.find_element(*StandardSearchLocators.SEARCH_FIELD)
        text_area.send_keys(text)
        assert self.is_element_present(*StandardSearchLocators.SUGGEST_TABLE), 'Suggest table not found'

    def tensor_first_in_search_result(self, address: str) -> None:
        '''
        Метод для проверки первого результатов поиска.
        Первый выводимый результат должен соответствовать параметру address
        :param address: str - искомый адрес
        :return: None
        '''
        text_area = self.browser.find_element(*StandardSearchLocators.SEARCH_FIELD)
        text_area.send_keys('Тензор\n')
        first_link = self.browser.find_element(*StandardSearchLocators.FIRST_LINK_IN_RESULTS_TABLE).get_attribute("href")
        assert first_link == address, 'The first link in the search results does not match the address passed'

