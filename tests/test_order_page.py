import pytest
import allure
import data
from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestOrderPages:
    @allure.title('Проверка оформления аренды самоката через кнопку Заказать вверху страницы')
    @allure.description('Проверка оформления аренды самоката двумя наборами тестовых данных')
    @pytest.mark.parametrize('name, surname, address, metro, number', [*data.TestPersonalData.test_personal_data])
    def test_order_button_on_top(self, driver, name, surname, address, metro, number):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.click_button_cookie()
        home_page.click_button_order_on_top()
        order_page.input_personal_date(name, surname, address, metro, number)
        text_order = order_page.successful_order_modal()
        assert "Заказ оформлен" in text_order

    @allure.title('Проверка оформления аренды самоката через кнопку Заказать в середине страницы')
    @allure.description('Проверка оформления аренды самоката двумя наборами тестовых данных')
    @pytest.mark.parametrize('name, surname, address, metro, number', [*data.TestPersonalData.test_personal_data])
    def test_order_button_below(self, driver, name, surname, address, metro, number):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.click_button_cookie()
        home_page.click_button_order_below()
        order_page.input_personal_date(name, surname, address, metro, number)
        text_order = order_page.successful_order_modal()
        assert "Заказ оформлен" in text_order
