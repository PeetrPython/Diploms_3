from pages.base_page import BasePage
import locators.account_page_locators as locators
import allure

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получение текста заголовка формы логина')
    def get_login_form_text(self):
        return self.get_text_from_element(locators.LOGIN_FORM_TITLE)

    @allure.step('Ждём появления формы логина')
    def wait_login_form(self):
        self.find_element_with_wait(locators.LOGIN_FORM_TITLE)

    @allure.step('Ждём загрузки страницы')
    def wait_page_ready(self):
        self.find_element_with_wait(locators.ORDER_HISTORY_BUTTON)

    @allure.step('Получение текста заголовка формы логина')
    def fill_login_form(self, email, password):
        self.add_text_to_element(locators.LOGIN_FORM_EMAIL_INPUT, email)
        self.add_text_to_element(locators.LOGIN_FORM_PASSWORD_INPUT, password)
        self.click_to_element(locators.LOGIN_FORM_BUTTON)

    @allure.step('Кликаем по кнопке "История заказов"')
    def go_to_orders_history(self):
        self.click_to_element(locators.ORDER_HISTORY_BUTTON)

    @allure.step('Получаем текст активного раздела')
    def get_active_item_text(self):
        return self.get_text_from_element(locators.ACTIVE_ITEM)

    @allure.step('Ждём переход в раздел "История заказов"')
    def wait_orders_history_transition(self):
        self.find_element_with_wait(locators.HISTORY_LIST_ACTIVE_ITEM)

    @allure.step('Нажимаем на кнопку "Выход"')
    def logout(self):
        self.click_to_element(locators.LOGOUT_BUTTON)

    @allure.step('Кликаем на ссылку "Восстановить пароль"')
    def go_to_password_recovery(self):
        self.click_to_element(locators.PASSWORD_RECOVERY_LINK)

    @allure.step('Получаем номер первого заказа из истории')
    def get_first_order_id(self):
        text = self.get_text_from_element(locators.FIRST_ORDER_ID)
        return text[2:]  # убираем символы '#' и '0'