from selenium.webdriver.common.by import By


class BasePageLocators:
    PASSWORD_ACTIVE = (
        By.XPATH, ".//*[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//*[text()='Личный Кабинет']")
    LOGIN_EMAIL_INPUT_FIELD = (By.XPATH, ".//*[@name='name']")
    LOGIN_PASSWORD_INPUT_FIELD = (By.XPATH, ".//*[@name='Пароль']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//*[text()='Конструктор']")
    ORDER_FEED = (By.XPATH, ".//*[text()='Лента Заказов']")
