import time
import allure

import pytest
from data import QuestionData, TestURL
from pages.header_page import HeaderPages
from pages.home_page import HomePages


class TestHomePage:
    @allure.title('Проверка соответствия вопроса и ответа')
    @allure.description('Проверяем, что при нажатии на вопрос открывается соответствующий текст ответа')
    @pytest.mark.parametrize('index, text_answer',
                             [(0, QuestionData.drop_down_text[0]), (1, QuestionData.drop_down_text[1]),
                              (2, QuestionData.drop_down_text[2]), (3, QuestionData.drop_down_text[3]),
                              (4, QuestionData.drop_down_text[4]), (5, QuestionData.drop_down_text[5]),
                              (6, QuestionData.drop_down_text[6]), (7, QuestionData.drop_down_text[7])])
    def test_check_answer(self, driver, index, text_answer):
        home_page = HomePages(driver)
        home_page.click_button_cookie()
        home_page.scroll_questions()
        question = home_page.click_question(index)
        answer = home_page.find_answer(index)
        assert text_answer[question] == answer

    @allure.title('Проверка перехода на сайт Самоката при нажатии на логотип Самокат')
    def test_check_scooter_logo_click(self, driver):
        header_page = HeaderPages(driver)
        home_page = HomePages(driver)
        home_page.click_button_order_on_top()
        header_page.click_scooter_logo()
        url = header_page.wait_for_url(TestURL.URL_MAIN_PAGE)
        assert TestURL.URL_MAIN_PAGE in url

    @allure.title('Проверка перехода на сайт Дзена при нажатии на логотип Яндекс')
    def test_check_yandex_logo_click(self, driver):
        header_page = HeaderPages(driver)
        header_page.click_yandex_logo()
        url = header_page.wait_for_url(TestURL.URL_DZEN)
        assert TestURL.URL_DZEN in url
