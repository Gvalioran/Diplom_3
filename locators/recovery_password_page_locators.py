from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class RecoveryPasswordPageLocators(BasePageLocators):
    BUTTON_RECOVERY_PASSWORD = (By.XPATH, ".//*[@href='/forgot-password']")
    BUTTON_RECOVERY = (By.XPATH, ".//*[text()='Восстановить']")
    BUTTON_LOGIN = (By.XPATH, ".//*[text()='Войти']")
    BUTTON_SAVE = (By.XPATH, ".//*[text()='Сохранить']")
    BUTTON_SHOW_PASSWORD = (By.XPATH, ".//*[@class='input__icon input__icon-action']")
    INPUT_EMAIL = (By.XPATH, ".//*[@class='text input__textfield text_type_main-default']")
