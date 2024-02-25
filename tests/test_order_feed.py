import allure

from constants.constants import Url
from pages.order_feed_page import OrderFeedPage


@allure.story('Тесты ленты заказов')
class TestsOrderFeed:
    @allure.title('Тест всплывающего окна с деталями заказа')
    def test_order_details(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.transition_site(Url.BASE_URL)
        order_feed_page.transition_to_order_feed()
        order_feed_page.click_to_order()
        result = order_feed_page.get_class_pop_up_window_order()
        assert "opened" in result

    @allure.title('Тест отображения заказа пользователя в ленте заказов и в истории заказов')
    def test_displaying_user_order_in_order_feed(self, driver, user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.transition_site(Url.LOGIN)
        order_feed_page.login_to_account(user["email"], user["password"])
        order_feed_page.transferring_ingredient_constructor()
        order_feed_page.click_button_place_an_order()
        num_order = order_feed_page.get_num_order()
        order_feed_page.click_button_close_pop_up_window()
        order_feed_page.transition_to_order_feed()
        assert order_feed_page.searching_item_by_order_number(num_order)
        order_feed_page.transition_to_personal_account()
        order_feed_page.transition_to_order_history()
        assert order_feed_page.searching_item_by_order_number(num_order)

    @allure.title('Тест увеличения счетчика выполненных заказов за все время')
    def test_increasing_counter_all_orders(self, driver, user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.transition_site(Url.FEED)
        result1 = order_feed_page.get_num_all_orders()
        order_feed_page.transition_site(Url.LOGIN)
        order_feed_page.login_to_account(user["email"], user["password"])
        order_feed_page.transferring_ingredient_constructor()
        order_feed_page.click_button_place_an_order()
        order_feed_page.transition_site(Url.FEED)
        result2 = order_feed_page.get_num_all_orders()
        assert int(result1) + 1 == int(result2)

    @allure.title('Тест увеличения счетчика выполненных заказов за сегодня')
    def test_increasing_counter_today_orders(self, driver, user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.transition_site(Url.FEED)
        result1 = order_feed_page.get_num_today_orders()
        order_feed_page.transition_site(Url.LOGIN)
        order_feed_page.login_to_account(user["email"], user["password"])
        order_feed_page.transferring_ingredient_constructor()
        order_feed_page.click_button_place_an_order()
        order_feed_page.transition_site(Url.FEED)
        result2 = order_feed_page.get_num_today_orders()
        assert int(result1) + 1 == int(result2)

    @allure.title('Тест отображения заказа пользователя в разделе "В работе"')
    def test_displaying_user_order_in_progress_section(self, driver, user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.transition_site(Url.LOGIN)
        order_feed_page.login_to_account(user["email"], user["password"])
        order_feed_page.transferring_ingredient_constructor()
        order_feed_page.click_button_place_an_order()
        num_order = order_feed_page.get_num_order()
        order_feed_page.click_button_close_pop_up_window()
        order_feed_page.transition_site(Url.FEED)
        num_order_at_work = order_feed_page.get_num_at_work_order()
        assert f"0{num_order}" == num_order_at_work
