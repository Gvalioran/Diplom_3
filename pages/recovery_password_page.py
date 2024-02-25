import allure

from pages.base_page import BasePage
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators


class RecoveryPasswordPage(BasePage):

    @allure.step("Переход к восстановлению пароля")
    def transition_to_password_recovery(self):
        self.find_element_located_click(RecoveryPasswordPageLocators.BUTTON_RECOVERY_PASSWORD)

    @allure.step("Ввод почты для восстановления пароля")
    def input_email_recovery(self, email):
        self.find_element_located_input(RecoveryPasswordPageLocators.INPUT_EMAIL, email)

    @allure.step("Клик по кнопке Восстановить")
    def click_recovery(self):
        self.find_element_located_click(RecoveryPasswordPageLocators.BUTTON_RECOVERY)

    @allure.step("Клик по кнопке показать пароль")
    def click_show_password_button(self):
        self.find_element_located_click(RecoveryPasswordPageLocators.BUTTON_SHOW_PASSWORD)

    @allure.step("Получить класс подсвечиваемого поля")
    def get_class_highlighted_field(self):
        return self.get_attribute(RecoveryPasswordPageLocators.PASSWORD_ACTIVE, "class")
