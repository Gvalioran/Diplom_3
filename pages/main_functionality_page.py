import allure

from pages.personal_account_page import PersonalAccountPage
from locators.main_functionality_locators import MainFunctionalityLocators


class MainFunctionalityPage(PersonalAccountPage):
    @allure.step("Переход к конструктору")
    def transition_to_constructor(self):
        self.find_element_located_click(MainFunctionalityLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход к ленте заказов")
    def transition_to_order_feed(self):
        self.find_element_located_click(MainFunctionalityLocators.ORDER_FEED)

    @allure.step("Клик по ингредиенту")
    def click_to_ingredient(self):
        self.find_element_located_click(MainFunctionalityLocators.INGREDIENT)

    @allure.step("Клик по кнопке закрытия всплывающего окна")
    def click_button_close_pop_up_window(self):
        self.find_element_located_click(MainFunctionalityLocators.POP_UP_WINDOW_CLOSE)

    @allure.step("Получение класса открытого всплывающего окна")
    def pop_up_window_opened_get_class(self):
        return self.get_attribute(MainFunctionalityLocators.POP_UP_WINDOW_OPEN, "class")

    @allure.step("Получение класса закрытого всплывающего окна")
    def pop_up_window_get_class(self):
        return self.get_attribute(MainFunctionalityLocators.POP_UP_WINDOW_CLOSE, "class")

    @allure.step("Перенос ингредиента в конструктор")
    def transferring_ingredient_constructor(self):
        ingredient = self.find_element_located(MainFunctionalityLocators.INGREDIENT)
        add_to_order = self.find_element_located(MainFunctionalityLocators.BURGER_CONSTRUCTOR)
        self.drag_and_drop(ingredient, add_to_order)

    @allure.step("Клик по кнопке оформить заказ")
    def click_button_place_an_order(self):
        self.find_element_located_click(MainFunctionalityLocators.PLACE_AN_ORDER)

    @allure.step("Получение счетчика ингредиента")
    def get_ingredient_counter(self):
        return self.get_element_text(MainFunctionalityLocators.INGREDIENT_COUNTER)

    @allure.step("Получение текста всплывающего окна оформления заказа")
    def get_text_pop_up_window(self):
        return self.get_element_text(MainFunctionalityLocators.POP_UP_WINDOW_ORDER)
