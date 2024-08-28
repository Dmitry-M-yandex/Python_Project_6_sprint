import allure
from helpers import RandomDate
from locators.order_page_locators import OrderPageLocators
from pages.base import Base


class OrderPage(Base, RandomDate):
    @allure.step('Заполняем поле Имя')
    def input_name(self, name):
        self.input_text(OrderPageLocators.FIELD_NAME, name)

    @allure.step('Заполняем поле Фамилия')
    def input_surname(self, surname):
        self.input_text(OrderPageLocators.FIELD_SURNAME, surname)

    @allure.step('Заполняем поле Адрес')
    def input_address(self, address):
        self.input_text(OrderPageLocators.FIELD_ADDRESS, address)

    @allure.step('Заполняем поле станция метро')
    def choosing_metro(self, metro):
        self.click_element(OrderPageLocators.FIELD_UNDERGROUND)
        self.input_text(OrderPageLocators.FIELD_UNDERGROUND, metro)
        self.click_element(OrderPageLocators.STATION_METRO)

    @allure.step('Заполняем поле Телефон')
    def input_phone_number(self, phone):
        self.input_text(OrderPageLocators.FIELD_PHONE, phone)

    @allure.step('Заполняем поле когда привезти самокат')
    def input_data(self):
        data = self.random_data()
        self.input_text(OrderPageLocators.FIELD_DATE, data)
        self.click_element(OrderPageLocators.TITLE_ABOUT_RENT)

    @allure.step('Заполняем поле период аренды')
    def input_rental_period(self):
        self.click_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        self.click_element(OrderPageLocators.RENT_DAY)

    @allure.step('Ожидаем окно об успешном оформлении заказа')
    def successful_order_modal(self):
        element = self.wait_element(OrderPageLocators.TITLE_ORDER_SUCCESS)
        return element.text

    @allure.step('Заполнение полей заказа и его оформление')
    def input_personal_date(self, name, surname, address, metro, number):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.choosing_metro(metro)
        self.input_phone_number(number)
        self.click_element(OrderPageLocators.BUTTON_NEXT)
        self.wait_element(OrderPageLocators.TITLE_ABOUT_RENT)
        self.input_data()
        self.input_rental_period()
        self.click_element(OrderPageLocators.BUTTON_ORDER)
        self.wait_element(OrderPageLocators.MODAL_CHECKOUT)
        self.click_element(OrderPageLocators.BUTTON_YES_CHECKOUT)
        self.wait_element(OrderPageLocators.TITLE_ORDER_SUCCESS)
