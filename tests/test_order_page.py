import pytest
import allure

from data import TestPersonalData
from pages.base_page import BasePages
from pages.home_page import HomePages
from pages.order_page import OrderPages


class TestOrderPages:
    @allure.title('Проверка оформления аренды самоката через кнопку Заказать вверху страницы')
    @allure.description('Проверка оформления аренды самоката двумя наборами тестовых данных')
    @pytest.mark.parametrize('name, surname, address, metro, number', [*TestPersonalData.test_personal_data])
    def test_order_button_on_top(self, driver, name, surname, address, metro, number):
        home_page = HomePages(driver)
        order_page = OrderPages(driver)
        base_page = BasePages(driver)
        base_page.click_button_cookie()
        home_page.click_button_order_on_top()
        order_page.input_personal_date(name, surname, address, metro, number)
        text_order = order_page.successful_order_modal()
        assert "Заказ оформлен" in text_order

    @allure.title('Проверка оформления аренды самоката через кнопку Заказать в середине страницы')
    @allure.description('Проверка оформления аренды самоката двумя наборами тестовых данных')
    @pytest.mark.parametrize('name, surname, address, metro, number', [*TestPersonalData.test_personal_data])
    def test_order_button_below(self, driver, name, surname, address, metro, number):
        home_page = HomePages(driver)
        order_page = OrderPages(driver)
        base_page = BasePages(driver)
        base_page.click_button_cookie()
        home_page.click_button_order_below()
        order_page.input_personal_date(name, surname, address, metro, number)
        text_order = order_page.successful_order_modal()
        assert "Заказ оформлен" in text_order
