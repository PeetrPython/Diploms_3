import time
from pages.base_page import BasePage
import allure
import locators.main_page_locators as locators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получаем текст заголовка страницы')
    def get_title_text(self):
        return self.get_text_from_element(locators.CONSTRUCTOR_TITLE)

    @allure.step('Ждём перехода на главную страницу')
    def wait_page_loading(self):
        self.find_element_with_wait(locators.CONSTRUCTOR_TITLE)

    @allure.step('Кликаем на ингредиент')
    def click_on_ingredient(self, ingredient_hash):
        locator = self.format_locator(locators.INGREDIENT_ELEM, ingredient_hash)
        self.click_to_element(locator)

    @allure.step('Получаем заголовок окна деталей ингредиента')
    def get_ingredient_details_header(self):
        return self.get_text_from_element(locators.DETAILS_DIALOG_TITLE)

    @allure.step('Дожидаемся появления окна деталей ингредиента')
    def wait_ingredient_details_window(self):
        self.find_element_with_wait(locators.DETAILS_DIALOG_TITLE)

    @allure.step('Кликаем на крестик окна деталей ингредиента')
    def close_ingredient_details_window(self):
        self.click_to_element(locators.DETAILS_DIALOG_CLOSE_BUTTON)

    @allure.step('Ждём закрытия окна деталей ингредиента ')
    def wait_ingredient_details_window_is_closed(self):
        return self.wait_invisibility_of_element(locators.DETAILS_DIALOG_TITLE)

    @allure.step('Получаем значения счетчика ингредиента')
    def get_ingredient_counter_value(self, ingredient_hash):
        counter_locator = self.format_locator(locators.INGREDIENT_ELEM_COUNTER, ingredient_hash)
        return int(self.get_text_from_element(counter_locator))

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredients_to_order(self, ingredient_hash):
        ingredient_locator = self.format_locator(locators.INGREDIENT_ELEM, ingredient_hash)
        self.drag_and_drop(ingredient_locator, locators.ORDER_BASKET)

    @allure.step('Кликаем по кнопке "Оформить заказ"')
    def click_order_button(self):
        self.click_to_element(locators.ORDER_BUTTON)

    @allure.step('Получаем заголовок окна завершения заказа')
    def get_order_finish_id_header(self):
        return self.get_text_from_element(locators.ORDER_WINDOW_ID_HEADER)

    @allure.step('Ждём появления окна завершения заказа')
    def wait_order_finish(self):
        self.wait_correct_order_number(locators.ORDER_NUMBER)

    @allure.step('Получаем id заказа')
    def get_order_id(self):
        return self.wait_correct_order_number(locators.ORDER_NUMBER)

    @allure.step('Закрываем окно завершения заказа')
    def close_order_finish_window(self):
        self.click_to_element(locators.ORDER_FINISH_WINDOW_CLOSE_BUTTON)