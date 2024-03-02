import allure

from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccountPage(BasePage):

    @allure.step("Переход к личному кабинету")
    def transition_to_personal_account(self):
        self.find_element_located_click(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Вход в аккаунт")
    def login_to_account(self, data):
        self.find_element_located_input(PersonalAccountLocators.LOGIN_EMAIL_INPUT_FIELD, data["email"])
        self.find_element_located_input(PersonalAccountLocators.LOGIN_PASSWORD_INPUT_FIELD, data["password"])
        self.find_element_located_click(PersonalAccountLocators.ENTER_TO_ACCOUNT)

    @allure.step("Переход в историю заказов")
    def transition_to_order_history(self):
        self.find_element_located_click(PersonalAccountLocators.ORDER_HISTORY)

    @allure.step("Выход из аккаунта")
    def logout_account(self):
        self.find_element_located_click(PersonalAccountLocators.LOGOUT_BUTTON)

    @allure.step("Получить атрибут кнопки история заказов")
    def get_the_order_history_button_attribute(self):
        return self.get_attribute(PersonalAccountLocators.ORDER_HISTORY, "aria-current")

    @allure.step("Поиск элемента войти в аккаунт")
    def search_log_in_account_item(self):
        return self.find_element_located(PersonalAccountLocators.ENTER_TO_ACCOUNT)
