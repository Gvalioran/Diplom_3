import allure

from constants.constants import Url
from pages.recovery_password_page import RecoveryPasswordPage


@allure.story('Тесты страницы восстановления пароля')
class TestsPasswordRecovery:
    @allure.title('Тест перехода форму восстановления пароля')
    def test_password_recovery_form_transition(self, driver):
        password_recovery_page = RecoveryPasswordPage(driver)
        password_recovery_page.transition_site(Url.LOGIN)
        password_recovery_page.transition_to_password_recovery()
        current_url = password_recovery_page.current_url()
        assert current_url == Url.FORGOT_PASSWORD

    @allure.title('Тест ввода почты для восстановления и клик по кнопке "Восстановить пароль"')
    def test_entering_recovery_mail_and_clicking_restore_button(self, driver, user):
        password_recovery_page = RecoveryPasswordPage(driver)
        password_recovery_page.transition_site(Url.FORGOT_PASSWORD)
        password_recovery_page.input_email_recovery(user["email"])
        password_recovery_page.click_recovery()
        password_recovery_page.expectation_url(Url.RESET_PASSWORD)
        current_url = password_recovery_page.current_url()
        assert current_url == Url.RESET_PASSWORD

    @allure.title('Тест "подсвечивания" поля ввода пароля для страницы восстановления пароля')
    def test_highlighting_password_field_password_recovery_page(self, driver, user):
        password_recovery_page = RecoveryPasswordPage(driver)
        password_recovery_page.transition_site(Url.FORGOT_PASSWORD)
        password_recovery_page.input_email_recovery(user["email"])
        password_recovery_page.click_recovery()
        password_recovery_page.click_show_password_button()
        result = password_recovery_page.get_class_highlighted_field()
        assert "status_active" in result
