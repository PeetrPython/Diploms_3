from pages.base_page import BasePage
import allure
import locators.orders_feed_page_locators as locators


class OrdersFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получение текста заголовка страницы')
    def get_title_text(self):
        return self.get_text_from_element(locators.ORDERS_FEED_TITLE)

    @allure.step('Получение загрузки страницы')
    def wait_orders_feed(self):
        return self.find_element_with_wait(locators.ORDERS_FEED_TITLE)

    @allure.step('Кликнуть на первый заказ')
    def click_on_first_order(self):
        return self.click_to_element(locators.FIRST_ORDER_CARD)

    @allure.step('Ждём появления окна деталей заказа')
    def wait_order_details_window(self):
        return self.find_element_with_wait(locators.ORDER_DETAILS_WINDOW)

    @allure.step('Получаем значение счётчика заказов за сегодня')
    def get_today_counter(self):
        return int(self.get_text_from_element(locators.ORDER_COUNTER_TODAY))

    @allure.step('Получаем значение счётчика заказов за всё время')
    def get_all_time_counter(self):
        return int(self.get_text_from_element(locators.ORDER_COUNTER_ALL_TIME))

    @allure.step('Ищем заказ с нужным номером в ленте')
    def find_order_id_text(self, order_id):
        locator = self.format_locator(locators.ORDER_ID_ELEMENT, order_id)
        return self.get_text_from_element(locator)

    @allure.step('Ищем заказ с нужным номером в списке "В работе"')
    def find_order_id_in_work_list(self, order_id):
        locator = self.format_locator(locators.ORDER_ID_IN_WORK, order_id)
        return self.find_element_with_wait(locator, 30).text
