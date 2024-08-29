import allure
from locators.home_page_locators import HomePageLocators
from pages.base import Base


class HomePage(Base):
    @allure.step('Скролим до раздела "Вопросы о важном"')
    def scroll_questions(self):
        self.scroll_element(HomePageLocators.TITLE_QUESTION)

    @allure.step('Кликаем на вопрос')
    def click_question(self, index):
        selector, locator = HomePageLocators.QUESTION_DROP_DOWN_LIST
        locator = locator.format(index)
        self.wait_element((selector, locator))
        self.click_element((selector, locator))
        return self.wait_element((selector, locator)).get_attribute("id")

    @allure.step('Ищем ответ на вопрос')
    def find_answer(self, index):
        selector, locator = HomePageLocators.ANSWER_DROP_DOWN_LIST
        locator = locator.format(index)
        element = self.wait_element((selector, locator))
        return element.text

    @allure.step('Кликаем на кнопку Заказать вверху страницы')
    def click_button_order_on_top(self):
        self.wait_element_clickable(HomePageLocators.BUTTON_ORDER_ON_TOP)
        self.click_element(HomePageLocators.BUTTON_ORDER_ON_TOP)

    @allure.step('Кликаем на кнопку Заказать в середине страницы')
    def click_button_order_below(self):
        self.scroll_element(HomePageLocators.BUTTON_ORDER_BELOW)
        self.wait_element_clickable(HomePageLocators.BUTTON_ORDER_BELOW)
        self.click_element(HomePageLocators.BUTTON_ORDER_BELOW)
