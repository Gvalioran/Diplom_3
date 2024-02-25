from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class MainFunctionalityLocators(BasePageLocators):
    INGREDIENT = (By.XPATH, ".//*[@alt='Флюоресцентная булка R2-D3']")
    POP_UP_WINDOW_OPEN = (By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    POP_UP_WINDOW_CLOSED = (By.XPATH, ".//section[@class='Modal_modal__P3_V5']")
    POP_UP_WINDOW_CLOSE = (By.XPATH, ".//*[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    BURGER_CONSTRUCTOR = (By.XPATH, ".//*[@class='BurgerConstructor_basket__list__l9dp_']")
    INGREDIENT_COUNTER = (By.XPATH, ".//ul[1]/a[1]/div[1]/p")
    PLACE_AN_ORDER = (By.XPATH, ".//*[text()='Оформить заказ']")
    POP_UP_WINDOW_ORDER = (By.XPATH, ".//*[@class='undefined text text_type_main-medium mb-15']")