import data
import allure


@allure.suite('Тесты страницы восстановления пароля')
class TestPasswordRecoveryPage:
    @allure.title('Переход в раздел "Восстановление пароля"')
    @allure.description('Переходим в личный кабинет, из него переходим на страницу восстановления пароля, '
                        'проверяем успешность перехода')
    def test_go_to_password_recovery(self, header_page, account_page, password_recovery_page):
        header_page.move_to_account()
        account_page.wait_login_form()

        account_page.go_to_password_recovery()
        assert password_recovery_page.get_title_text() == data.PASSWORD_RECOVERY_HEADER_TEXT

    @allure.title('Ввод почты для восстановление пароля')
    @allure.description('Переходим в личный кабинет, из него переходим на страницу восстановления пароля, '
                        'вводим почту, кликаем на кнопку "Восстановить", ждём появления поля ввода нового пароля')
    def test_fill_email_form(self, header_page, account_page, password_recovery_page, user_credentials):
        header_page.move_to_account()
        account_page.wait_login_form()

        account_page.go_to_password_recovery()
        password_recovery_page.wait_page_ready()

        password_recovery_page.fill_email_form(user_credentials['email'])

        assert password_recovery_page.find_new_password_field() is not None

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    @allure.description('Переходим в личный кабинет, из него переходим на страницу восстановления пароля, '
                        'вводим почту, кликаем на кнопку "Восстановить", ждём появления поля ввода нового пароля, '
                        'кликаем на кнопку показать/скрыть пароль и проверяем, что она подсвечивается')
    def test_new_password_field_become_active(self, header_page, account_page,
                                              password_recovery_page, user_credentials):
        header_page.move_to_account()
        account_page.wait_login_form()

        account_page.go_to_password_recovery()
        password_recovery_page.wait_page_ready()

        password_recovery_page.fill_email_form(user_credentials['email'])
        assert password_recovery_page.find_new_password_field() is not None

        assert password_recovery_page.is_password_field_active() is False

        password_recovery_page.click_open_hide_password_button()
        assert password_recovery_page.is_password_field_active() is True