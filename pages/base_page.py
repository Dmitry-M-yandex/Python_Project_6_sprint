import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import HomePageLocators


class BasePages:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем {locator}')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем {locator} и элемент кликабелен')
    def wait_element_clickable(self, locator):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return element

    @allure.step('Кликаем на {locator}')
    def click_element(self, locator):
        self.wait_element_clickable(locator).click()

    @allure.step('Скролим к {locator}')
    def scroll_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидаем окно и кликаем на кнопку принятия кук')
    def click_button_cookie(self):
        self.wait_element_clickable(HomePageLocators.BUTTON_COOKIE)
        self.click_element(HomePageLocators.BUTTON_COOKIE)

    @allure.step('Печатаем {text} в {locator}')
    def input_text(self, locator, text):
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Ожидаем URL текущей страницы')
    def wait_url_contains(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(url))
        return self.driver.current_url

    @allure.step('Делаем активной вкладкой последний открытый сайт')
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

