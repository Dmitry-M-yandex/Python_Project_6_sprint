import random

import pytest
from selenium import webdriver

from data import TestURL


@pytest.fixture
def driver():
    """Фикстура для запуска браузера Firefox."""
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(TestURL.URL_MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def random_email():
    email_registration = f'dmitrymalakhov12_{random.randint(100, 999)}@yandex.ru'
    yield email_registration
