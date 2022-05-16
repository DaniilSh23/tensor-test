from .base_search import BaseSearch
from .locators import PicturesSearchLocators


class PicturesSearch(BaseSearch):
    '''Класс для работы с разделом изображений'''

    def should_be_image_link(self) -> None:
        '''
        Метод для проверки наличия ссылки для перехода в раздел картинок
        :return: None
        '''
        assert self.is_element_present(*PicturesSearchLocators.IMAGE_LINK), 'Image link not found.'

    def input_and_check_suggest(self, text: str) -> None:
        '''
        Метод для проверки наличия таблицы с подсказками
        :param text: str - текст, вводимый в поле для поиска
        :return: None
        '''
        text_area = self.browser.find_element(*PicturesSearchLocators.IMAGE_LINK_INVALID)
        text_area.send_keys(text)
        assert self.is_element_present(*PicturesSearchLocators.IMAGE_LINK_INVALID), 'Suggest table not found'

    def check_url_address(self, address: str) -> None:
        '''
        Метод для проверки перехода по верному URL адресу.
        Проверяет вхождение подстроки в строку (заданный адрес, текущий адрес)
        :param address: str - заданный адрес
        :return: None
        '''
        image_section = self.browser.find_element(*PicturesSearchLocators.IMAGE_LINK)
        self.browser.get(image_section.get_attribute("href"))
        current_url = self.browser.current_url
        assert address in current_url, 'URL addresses do not match'

    def check_input_by_default_value(self) -> None:
        '''
        Метод для перехода на первую категорию изображений
        и проверки наличия названия категории в поле для поиска Яндекса.
        :return: None
        '''
        first_cat = self.browser.find_element(*PicturesSearchLocators.FIRST_IMAGE_CAT)
        first_cat.click()
        self.browser.get(self.browser.current_url)
        assert self.browser.find_element(*PicturesSearchLocators.INPUT_FORM).get_attribute('value'), \
            'Category name not found.'

    def check_open_first_image(self) -> str:
        '''
        Метод для клика по первой картинки и проверки, что она открылась
        :return: str
        '''
        first_image = self.browser.find_element(*PicturesSearchLocators.FIRST_IMAGE)
        first_image.click()
        open_image = self.browser.find_element(*PicturesSearchLocators.OPEN_IMAGE)
        image_src = open_image.get_attribute('src')
        assert image_src, 'Image not open'
        return image_src

    def switch_right_image_and_check_changes(self, left_image_src: str) -> None:
        '''
        Метод для переключения картинок вправо
        :return: None
        '''
        self.browser.find_element(*PicturesSearchLocators.SWITCH_RIGHT).click()
        open_image = self.browser.find_element(*PicturesSearchLocators.OPEN_IMAGE)
        right_image_src = open_image.get_attribute('src')
        assert left_image_src != right_image_src, 'the picture didnt move to the right'

    def switch_left_image_and_check_changes(self, left_image_src: str) -> None:
        '''
        Метод для переключения картинок влево
        :return: None
        '''
        self.browser.find_element(*PicturesSearchLocators.SWITCH_LEFT).click()
        checking_left_image_src = self.browser.find_element(*PicturesSearchLocators.OPEN_IMAGE).get_attribute('src')
        assert left_image_src == checking_left_image_src, 'the picture didnt move to the left'

