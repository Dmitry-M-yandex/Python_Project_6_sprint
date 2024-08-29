import allure
from locators.home_page_locators import HomePageLocators
from pages.base import Base


class HeaderPage(Base):

    @allure.step('Кликаем на лого Яндекс')
    def click_yandex_logo(self):
        self.click_element(HomePageLocators.HEADER_LOGO_YANDEX)

    @allure.step('Кликаем на лого Самокат')
    def click_scooter_logo(self):
        self.click_element(HomePageLocators.HEADER_LOGO_SCOOTER)

    @allure.step('Ожидаем, что открытая страница будет содержать {url}')
    def wait_for_url(self, url):
        self.switch_to_last_window()
        url = self.wait_url_contains(url)
        return url
