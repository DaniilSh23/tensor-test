import pytest
from .pages.pictures_search import PicturesSearch
from .pages.standard_search import StandardSearch
from loguru import logger


# создаём журнал логирования, который будет обновляться каждые 7 дней
logger.add("runtime_{time}.log", retention="7 days")


@pytest.mark.standard
class TestStandardSearch():
    '''Класс, объединяющий тесты для базового поиска в Яндексе'''
    link = 'https://yandex.ru/'

    @logger.catch
    def test_presence_of_search_field(self, browser):
        '''
        Тест для проверки наличия поля для поиска
        :param browser: - фикстура - объект браузера
        :return: None
        '''
        page = StandardSearch(browser, self.link)
        logger.info('START open METHOD')
        page.open()
        logger.info('START should_be_search_box METHOD')
        page.should_be_search_box()

    @logger.catch
    def test_input_and_check_suggest(self, browser):
        '''
        Тест для проверки наличия таблицы с подсказками в поле для поиска
        :param browser: - фикстура - объект браузера
        :return: None
        '''
        page = StandardSearch(browser, self.link)
        logger.info('START input_and_check_suggest METHOD')
        page.input_and_check_suggest(text='Тензор')

    @logger.catch
    def test_search_result_table(self, browser):
        '''
        Тест для проверки наличия искомого URL адреса в первом объекте вывода результатов поиска.
        :param browser: - фикстура - объект браузера
        :return: None
        '''
        page = StandardSearch(browser, self.link)
        logger.info('START open METHOD')
        page.open()
        logger.info('START tensor_first_in_search_result METHOD')
        page.tensor_first_in_search_result(address='https://tensor.ru/')


@pytest.mark.image
class TestPictures():
    '''Класс, объединяющий тесты для поиска в Яндексе по картинкам'''
    link = 'https://yandex.ru/'

    @logger.catch
    def test_picture_link_is_exist(self, browser):
        '''
        Тест для проверки наличия ссылки на раздел с картинками в Яндексе.
        :param browser: - фикстура - объект браузера
        :return: None
        '''
        page = PicturesSearch(browser, self.link)
        logger.info('START open METHOD')
        page.open()
        logger.info('START should_be_image_link METHOD')
        page.should_be_image_link()

    @logger.catch
    def test_check_current_url_address(self, browser):
        '''
        Тест для проверки правильности адреса, по которому выполнен переход.
        :param browser: - фикстура - объект браузера
        :return: None
        '''
        page = PicturesSearch(browser, self.link)
        address = 'https://yandex.ru/images/'
        logger.info('START check_url_address METHOD')
        page.check_url_address(address=address)

    @logger.catch
    def test_select_first_category_and_check_input_value(self, browser):
        '''
        Тест для клика по первой категории картинок
        и проверки наличие названия категории в поле для поиска.
        :param browser: - фикстура - объект браузера
        :return: None
        '''
        page = PicturesSearch(browser, self.link)
        logger.info('START check_input_by_default_value METHOD')
        page.check_input_by_default_value()

    @logger.catch
    def test_open_first_image_and_switch_them(self, browser):
        '''
        Тест для проверки открытия первой картинки
        и переключения их по кнопкам интерфейса
        :param browser: - фикстура - объект браузера
        :return: None
        '''
        page = PicturesSearch(browser, self.link)
        logger.info('START check_open_first_image METHOD')
        left_image_src = page.check_open_first_image()
        logger.info('START switch_right_image_and_check_changes METHOD')
        page.switch_right_image_and_check_changes(left_image_src)
        logger.info('START switch_left_image_and_check_changes METHOD')
        page.switch_left_image_and_check_changes(left_image_src)
