from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class OrderFeedLocators(BasePageLocators):
    ORDERS = (By.XPATH, ".//*[@class='OrderFeed_list__OLh59']")
    POP_UP_WINDOW_ORDER = (By.XPATH, ".//*[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    NUM_ORDER = (By.XPATH, ".//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text "
                           "text_type_digits-large mb-8']")
    ALL_ORDERS = (By.XPATH, ".//div/div/div/div[2]/p[2]")
    ORDERS_TODAY = (By.XPATH, ".//div/div/div/div[3]/p[2]")
    AT_WORK = (By.XPATH, ".//div[1]/ul[2]/li")
