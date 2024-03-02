import allure

from constants.urls import Url
from pages.personal_account_page import PersonalAccountPage


@allure.story('Тесты личного кабинета')
class TestsPersonalAccount:
    @allure.title('Тест перехода в личный кабинет')
    def test_transition_personal_account(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.transition_site(Url.BASE_URL)
        personal_account_page.transition_to_personal_account()
        personal_account_page.expectation_url(Url.LOGIN)
        current_url = personal_account_page.current_url()
        assert current_url == Url.LOGIN

    @allure.title('Тест перехода в историю заказов')
    def test_going_order_history(self, driver, user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.transition_site(Url.LOGIN)
        personal_account_page.login_to_account(user)
        personal_account_page.transition_to_personal_account()
        personal_account_page.transition_to_order_history()
        result = personal_account_page.get_the_order_history_button_attribute()
        assert result == "page"

    @allure.title('Тест выхода из аккаунта')
    def test_account_logout_test(self, driver, user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.transition_site(Url.LOGIN)
        personal_account_page.login_to_account(user)
        personal_account_page.transition_to_personal_account()
        personal_account_page.logout_account()
        assert personal_account_page.search_log_in_account_item()


