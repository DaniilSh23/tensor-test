from selenium.webdriver.common.by import By


class StandardSearchLocators():
    '''
    Локаторы для базового поиска  в Яндексе
    '''
    SEARCH_FIELD = (By.CSS_SELECTOR, ".input__control.input__input.mini-suggest__input")
    SEARCH_FIELD_INVALID = (By.CSS_SELECTOR, "._явно_мимо_.input__control.input__input.mini-suggest__input")
    SUGGEST_TABLE = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile')
    SUGGEST_TABLE_INVALID = (By.CSS_SELECTOR, '._явно_мимо_.mini-suggest__popup.mini-suggest__popup_svg_yes.mini'
                                              '-suggest__popup_theme_tile')
    FIRST_LINK_IN_RESULTS_TABLE = (By.CSS_SELECTOR, '[data-cid="0"] a')
    FIRST_LINK_IN_RESULTS_TABLE_INVALID = (By.CSS_SELECTOR, '_явно_мимо_[data-cid="0"] a')


class PicturesSearchLocators():
    '''
    Локаторы для поиска по картинке в Яндексе
    '''
    IMAGE_LINK = (By.CSS_SELECTOR, '[data-id="images"]')
    IMAGE_LINK_INVALID = (By.CSS_SELECTOR, '_явно_мимо.ru_[data-id="images"]')
    FIRST_IMAGE_CAT = (By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0')
    FIRST_IMAGE_CAT_INVALID = (By.CSS_SELECTOR, '_явно_мимо.ru_.PopularRequestList-Item.PopularRequestList-Item_pos_0')
    INPUT_FORM = (By.CSS_SELECTOR, '.input__control.mini-suggest__input')
    FIRST_IMAGE = (By.CSS_SELECTOR, '.serp-item__preview a')
    OPEN_IMAGE = (By.CSS_SELECTOR, '.MMImage-Preview')
    SWITCH_RIGHT = (By.CSS_SELECTOR, '.MediaViewer_theme_fiji-ButtonNext')
    SWITCH_LEFT = (By.CSS_SELECTOR, '.MediaViewer_theme_fiji-ButtonPrev')
    SWITCH_RIGHT_INVALID = (By.CSS_SELECTOR, '.MediaViewer_theme_fiji-ButtonPrev')
    SWITCH_LEFT_INVALID = (By.CSS_SELECTOR, '.MediaViewer_theme_fiji-ButtonNext')