from selenium.webdriver.common.by import By

# Кнопка "Восстановить"
PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")

# Заголовок "Восстановление пароля"
PASSWORD_RECOVERY_TITLE = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")

# Поле "Email"
EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')

# Кнопка "Сохранить"
SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')

# Кнопка "Показать/скрыть пароль"
BUTTON_PASSWORD_SHOW = (By.XPATH, "//div[@class='input__icon input__icon-action']")

# Поле "Введите новый пароль"
NEW_PASSWORD_FIELD = (By.XPATH, '//input[@name="Введите новый пароль"]')

# Элемент div, в котором лежит поле "Введите новый пароль"
NEW_PASSWORD_PARENT_DIV = (By.XPATH, '//div[input[@name="Введите новый пароль"]]')