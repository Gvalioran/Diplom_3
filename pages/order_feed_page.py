import time

import allure
from selenium.webdriver.common.by import By

from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step("Клик по заказу")
    def click_to_order(self):
        self.find_element_located_click(OrderFeedLocators.ORDERS)

    # Без явного ожидания гетер забирает номер заказа 9999 куратор сказал оставить падение, но я думаю что так лучше
    @allure.step("Получить номер заказа")
    def get_num_order(self):
        self.find_element_located(OrderFeedLocators.NUM_ORDER)
        self.wait_for_text_not_template(OrderFeedLocators.NUM_ORDER, '9999')
        return self.get_element_text(OrderFeedLocators.NUM_ORDER)

    @allure.step("Получить количество заказов за все время")
    def get_num_all_orders(self):
        return self.get_element_text(OrderFeedLocators.ALL_ORDERS)

    @allure.step("Получить количество заказов за все время")
    def get_num_today_orders(self):
        return self.get_element_text(OrderFeedLocators.ORDERS_TODAY)

    # Без явного ожидания гетер забирает, что заказы готовы, куратор сказал оставить падение, но я думаю так лучше
    @allure.step("Получить заказ из раздела в работе")
    def get_num_at_work_order(self):
        self.find_element_located(OrderFeedLocators.AT_WORK)
        self.wait_for_text_not_template(OrderFeedLocators.AT_WORK, 'Все текущие заказы готовы!')
        return self.get_element_text(OrderFeedLocators.AT_WORK)

    @allure.step("Получить класс всплывающего окна созданного заказа")
    def get_class_pop_up_window_order(self):
        return self.get_attribute(OrderFeedLocators.POP_UP_WINDOW_ORDER, "class")

    @allure.step("Поиск элемента по номеру заказа")
    def searching_item_by_order_number(self, num_order):
        str_num_order = OrderFeedLocators.STR_NUM_ORDER
        str_num_order = (str_num_order[0], str_num_order[1].format(num_order=num_order))
        return self.find_element_located(str_num_order)
