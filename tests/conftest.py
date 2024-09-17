from selenium import webdriver
import pytest
import allure
import data
import helpers
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.orders_feed_page import OrdersFeedPage

@allure.step('Открываем окно браузера')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    else:
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    driver.implicitly_wait(30)
    driver.set_window_size(1920, 1080)
    driver.get(data.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def header_page(driver):
    return HeaderPage(driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def account_page(driver):
    return AccountPage(driver)

@pytest.fixture
def orders_feed_page(driver):
    return OrdersFeedPage(driver)

@pytest.fixture
def password_recovery_page(driver):
    return PasswordRecoveryPage(driver)

@pytest.fixture
def user_credentials():
    credentials = helpers.generate_new_user_credentials()
    helpers.create_user(credentials)
    yield credentials
    helpers.delete_user(credentials)