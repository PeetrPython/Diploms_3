import data
import allure


@allure.suite('Тесты ленты заказов')
class TestsOrdersFeedPage:
    @allure.title('Увеличение счётчика "Выполнено за всё время"')
    @allure.description('Проверяем, что счётчик "Выполнено за всё время" увеличивается после оформления заказа')
    def test_increase_all_time_order_counter(self, header_page, account_page,
                                             main_page, orders_feed_page, user_credentials):
        # логинимся
        header_page.move_to_account()
        account_page.wait_login_form()
        account_page.fill_login_form(user_credentials['email'], user_credentials['password'])
        main_page.wait_page_loading()

        # открываем ленту и получаем текущее значение счётчика
        header_page.move_to_orders_feed()
        orders_feed_page.wait_orders_feed()
        counter_value_before_order = orders_feed_page.get_all_time_counter()

        # возвращаемся на главную страницу и делаем заказ
        header_page.move_to_constructor()
        main_page.wait_page_loading()
        main_page.add_ingredients_to_order(data.INGREDIENT_HASH)
        main_page.click_order_button()
        main_page.wait_order_finish()
        main_page.close_order_finish_window()

        # переходим опять в ленту и снова получаем значение счётчика
        header_page.move_to_orders_feed()
        orders_feed_page.wait_orders_feed()
        counter_value_after_order = orders_feed_page.get_all_time_counter()

        assert counter_value_after_order > counter_value_before_order

    @allure.title('Увеличение счётчика "Выполнено за сегодня"')
    @allure.description('Проверяем, что счётчик "Выполнено за сегодня" увеличивается после оформления заказа')
    def test_increase_today_order_counter(self, header_page, account_page,
                                          main_page, orders_feed_page, user_credentials):
        # логинимся
        header_page.move_to_account()
        account_page.wait_login_form()
        account_page.fill_login_form(user_credentials['email'], user_credentials['password'])
        main_page.wait_page_loading()

        # открываем ленту и получаем текущее значение счётчика
        header_page.move_to_orders_feed()
        orders_feed_page.wait_orders_feed()
        counter_value_before_order = orders_feed_page.get_today_counter()

        # возвращаемся на главную страницу и делаем заказ
        header_page.move_to_constructor()
        main_page.wait_page_loading()
        main_page.add_ingredients_to_order(data.INGREDIENT_HASH)
        main_page.click_order_button()
        main_page.wait_order_finish()
        main_page.close_order_finish_window()

        # переходим опять в ленту и снова получаем значение счётчика
        header_page.move_to_orders_feed()
        orders_feed_page.wait_orders_feed()
        counter_value_after_order = orders_feed_page.get_today_counter()

        assert counter_value_after_order > counter_value_before_order

    @allure.title('Проверяем, что заказ из истории есть в ленте')
    @allure.description('Логинимся, выполняем заказ и проверяем, что он есть в истории и в ленте')
    def test_orders_from_history_exist_in_feed(self, header_page, account_page,
                                               main_page, orders_feed_page, user_credentials):
        # логинимся
        header_page.move_to_account()
        account_page.wait_login_form()
        account_page.fill_login_form(user_credentials['email'], user_credentials['password'])
        main_page.wait_page_loading()

        # делаем заказ
        main_page.add_ingredients_to_order(data.INGREDIENT_HASH)
        main_page.click_order_button()
        order_id = main_page.get_order_id()
        main_page.close_order_finish_window()

        # идём в историю заказов
        header_page.move_to_account()
        account_page.wait_page_ready()
        account_page.go_to_orders_history()
        history_order_id = account_page.get_first_order_id()

        assert history_order_id == order_id

        # идём в ленту заказов
        header_page.move_to_orders_feed()
        orders_feed_page.wait_orders_feed()
        feed_order_id_text = orders_feed_page.find_order_id_text('0' + order_id)

        # убираем решётку в начале строки и 0
        assert feed_order_id_text[2:] == order_id

    @allure.title('Проверяем, что заказ есть в разделе "в работе"')
    @allure.description('Логинимся, выполняем заказ и проверяем, что он есть в разделе "в работе" ленты заказов')
    def test_order_is_in_work_list(self, header_page, account_page,
                                   main_page, orders_feed_page, user_credentials):
        # логинимся
        header_page.move_to_account()
        account_page.wait_login_form()
        account_page.fill_login_form(user_credentials['email'], user_credentials['password'])
        main_page.wait_page_loading()

        # делаем заказ
        main_page.add_ingredients_to_order(data.INGREDIENT_HASH)
        main_page.click_order_button()
        order_id = main_page.get_order_id()
        main_page.close_order_finish_window()

        # идём в ленту заказов
        header_page.move_to_orders_feed()
        orders_feed_page.wait_orders_feed()
        # ищем заказ в разделе "В работе"
        id_text = orders_feed_page.find_order_id_in_work_list(order_id)
        # в тексте 2 строки "0" и id, поэтому проверяем через in
        assert order_id in id_text

    @allure.title('Открываем окно с деталями заказа')
    @allure.description('Логинимся, выполняем заказ, переходим в ленту заказов, '
                        'кликаем на заказе и проверяем, что открылось окно с деталями')
    def test_open_order_info(self, header_page, account_page,
                                   main_page, orders_feed_page, user_credentials):
        # логинимся
        header_page.move_to_account()
        account_page.wait_login_form()
        account_page.fill_login_form(user_credentials['email'], user_credentials['password'])
        main_page.wait_page_loading()

        # делаем заказ
        main_page.add_ingredients_to_order(data.INGREDIENT_HASH)
        main_page.click_order_button()
        main_page.get_order_id()
        main_page.close_order_finish_window()

        # идём в ленту заказов
        header_page.move_to_orders_feed()
        orders_feed_page.wait_orders_feed()

        # кликаем на первом заказе
        orders_feed_page.click_on_first_order()

        assert orders_feed_page.wait_order_details_window() is not None