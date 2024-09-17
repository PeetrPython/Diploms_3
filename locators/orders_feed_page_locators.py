from selenium.webdriver.common.by import By

# Заголовок "Лента заказов"
ORDERS_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

# Первая карточка заказа
FIRST_ORDER_CARD = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]")

# Окно с деталями заказа
ORDER_DETAILS_WINDOW = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]")

# Значение счётчика "Выполнено за все время:"
ORDER_COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/../p[contains(@class, 'OrderFeed_number')]")

# Значение счётчика "Выполнено за сегодня:"
ORDER_COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/../p[contains(@class, 'OrderFeed_number')]")

# Шаблон элемента заданного id заказа
ORDER_ID_ELEMENT = (By.XPATH, "//p[text()='#{}' and contains(@class, 'text_type_digits')]")

# Шаблон для поиска заказа в списке "В работе"
ORDER_ID_IN_WORK = (By.XPATH, "//li[contains(text()[2], '{}')]")