from pages.base_page import BasePage
import locators.password_recovery_page_locators as locators
import allure


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получение текста заголовка страницы')
    def get_title_text(self):
        return self.get_text_from_element(locators.PASSWORD_RECOVERY_TITLE)

    @allure.step('Ждём перехода на страницу восстановления пароля')
    def wait_page_ready(self):
        self.find_element_with_wait(locators.PASSWORD_RECOVERY_TITLE)

    @allure.step('Вводим почту и кликаем на кнопку "Восстановить"')
    def fill_email_form(self, email):
        self.add_text_to_element(locators.EMAIL_FIELD, email)
        self.click_to_element(locators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Находим поле ввода нового пароля')
    def find_new_password_field(self):
        return self.find_element_with_wait(locators.NEW_PASSWORD_FIELD)

    @allure.step('Кликаем на кнопку показать/скрыть пароль')
    def click_open_hide_password_button(self):
         self.click_to_element(locators.BUTTON_PASSWORD_SHOW)

    @allure.step('Проверяем активно (подсвечивается) ли поле ввода нового пароля')
    def is_password_field_active(self):
        return 'input_status_active' in self.get_attribute(locators.NEW_PASSWORD_PARENT_DIV, 'class')