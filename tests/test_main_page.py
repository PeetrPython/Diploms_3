import time
import data
import allure


@allure.suite('Тесты главной страницы')
class TestsMainPage:
    @allure.title('Открытие окна информации об ингредиенте')
    @allure.description('Кликаем на ингредиенте, проверяем, что появилось окно с деталями')
    def test_open_ingredient_details_window(self, main_page):
        main_page.click_on_ingredient(data.INGREDIENT_HASH)
        time.sleep(1)
        assert main_page.get_ingredient_details_header() == data.INGREDIENT_DETAILS_HEADER_TEXT

    @allure.title('Закрытие окна информации об ингредиенте')
    @allure.description('Кликаем на ингредиенте, проверяем, что появилось окно с деталями, '
                        'закрываем окно: проверяем, что оно закрыто')
    def test_close_ingredient_details_window(self, main_page):
        main_page.click_on_ingredient(data.INGREDIENT_HASH)

        main_page.wait_ingredient_details_window()
        main_page.close_ingredient_details_window()
        time.sleep(1)
        assert main_page.wait_ingredient_details_window_is_closed()

    @allure.title('Увеличение счётчика ингредиента')
    @allure.description('Перетаскиваем ингредиент в корзину, проверяем, что увеличился счётчик данного ингредиента')
    def test_increase_ingredient_counter(self, main_page):
        counter = main_page.get_ingredient_counter_value(data.INGREDIENT_HASH)
        assert counter == 0

        main_page.add_ingredients_to_order(data.INGREDIENT_HASH)
        time.sleep(1)

        counter = main_page.get_ingredient_counter_value(data.INGREDIENT_HASH)
        assert counter == 2  # верх и низ бургера

    @allure.title('Оформление заказа')
    @allure.description('Логинимся и выполняем заказ')
    def test_make_order(self, header_page, main_page, account_page, user_credentials):
        header_page.move_to_account()
        account_page.wait_login_form()

        account_page.fill_login_form(user_credentials['email'], user_credentials['password'])
        main_page.wait_page_loading()

        main_page.add_ingredients_to_order(data.INGREDIENT_HASH)

        main_page.click_order_button()

        assert main_page.get_order_finish_id_header() == data.ORDER_FINISH_WINDOW_HEADER