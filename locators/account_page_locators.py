from selenium.webdriver.common.by import By

# Заголовок "Вход" формы логина
LOGIN_FORM_TITLE = (By.XPATH, "//h2[text()='Вход']")

# Поле "Email"
LOGIN_FORM_EMAIL_INPUT = (By.NAME, 'name')

# Поле "Пароль"
LOGIN_FORM_PASSWORD_INPUT = (By.NAME, 'Пароль')

# Кнопка "Войти"
LOGIN_FORM_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Ссылка "Восстановить пароль"
PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

# Кнопка "История заказов"
ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')

# Активный раздел личного кабинета
ACTIVE_ITEM = (By.XPATH, '//a[contains(@class, "Account_link_active")]')

# Активный раздел "История заказов"
HISTORY_LIST_ACTIVE_ITEM = (By.XPATH, '//a[contains(@class, "Account_link_active") and text()="История заказов"]')

# Список истории заказов
HISTORY_LIST = (By.XPATH, '//div[contains(@class, "OrderHistory_orderHistory")]')

# Кнопка "Выход"
LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')

# Номер первого заказа в истории
FIRST_ORDER_ID = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li[1]/a/div/p[1]")