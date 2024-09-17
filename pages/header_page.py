from pages.base_page import BasePage
import allure
import locators.header_page_locators as locators


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переходим на страницу "Лента заказов" по заголовку в хедере')
    def move_to_orders_feed(self):
        self.click_to_element(locators.ORDERS_FEED_HEADER)

    @allure.step('Переходим на главную страницу по кнопке в хедере')
    def move_to_constructor(self):
        self.click_to_element(locators.CONSTRUCTOR_BUTTON)

    @allure.step('Переходим по кнопке "Личный кабинет"')
    def move_to_account(self):
        self.click_to_element(locators.ACCOUNT_BUTTON)