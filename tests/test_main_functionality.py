import allure

from constants.constants import Url
from pages.main_functionality_page import MainFunctionalityPage


@allure.story('Тесты основного функционала')
class TestsMainFunctionality:
    @allure.title('Тест перехода в конструктор')
    def test_switching_constructor(self, driver):
        main_functionality_page = MainFunctionalityPage(driver)
        main_functionality_page.transition_site(Url.LOGIN)
        main_functionality_page.transition_to_constructor()
        current_url = main_functionality_page.current_url()
        assert current_url == Url.BASE_URL

    @allure.title('Тест перехода в ленту заказов')
    def test_switching_order_feed(self, driver):
        main_functionality_page = MainFunctionalityPage(driver)
        main_functionality_page.transition_site(Url.BASE_URL)
        main_functionality_page.transition_to_order_feed()
        current_url = main_functionality_page.current_url()
        assert current_url == Url.FEED

    @allure.title('Тест появления всплывающего окна')
    def test_pop_up_window_open(self, driver):
        main_functionality_page = MainFunctionalityPage(driver)
        main_functionality_page.transition_site(Url.BASE_URL)
        main_functionality_page.click_to_ingredient()
        result = main_functionality_page.pop_up_window_opened_get_class()
        assert "opened" in result

    @allure.title('Тест закрытия всплывающего окна')
    def test_pop_up_window_close(self, driver):
        main_functionality_page = MainFunctionalityPage(driver)
        main_functionality_page.transition_site(Url.BASE_URL)
        main_functionality_page.click_to_ingredient()
        main_functionality_page.click_button_close_pop_up_window()
        result = main_functionality_page.pop_up_window_get_class()
        assert "opened" not in result

    @allure.title('Тест счетчика ингредиента')
    def test_ingredient_counter(self, driver):
        main_functionality_page = MainFunctionalityPage(driver)
        main_functionality_page.transition_site(Url.BASE_URL)
        main_functionality_page.transferring_ingredient_constructor()
        result = main_functionality_page.get_ingredient_counter()
        assert result == "2"

    @allure.title('Тест оформления заказа')
    def test_checkout(self, driver, user):
        main_functionality_page = MainFunctionalityPage(driver)
        main_functionality_page.transition_site(Url.LOGIN)
        main_functionality_page.login_to_account(user["email"], user["password"])
        main_functionality_page.transferring_ingredient_constructor()
        main_functionality_page.click_button_place_an_order()
        result = main_functionality_page.get_text_pop_up_window()
        assert result == "идентификатор заказа"
