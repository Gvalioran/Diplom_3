from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class PersonalAccountLocators(BasePageLocators):
    ENTER_TO_ACCOUNT = (By.XPATH, ".//button[text()='Войти']")
    ORDER_HISTORY = (By.XPATH, ".//*[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, ".//*[text()='Выход']")
