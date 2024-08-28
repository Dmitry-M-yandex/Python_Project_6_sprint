from selenium.webdriver.common.by import By


class HomePageLocators:
    # Логотип Яндекса на главной странице сайта
    HEADER_LOGO_YANDEX = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")
    # Логотип Самокат на главной странице сайта
    HEADER_LOGO_SCOOTER = (By.XPATH, "//*[contains(@class,'Header_LogoScooter')]")
    # Локатор кнопки "да все привыкли" окна кук
    BUTTON_COOKIE = (By.ID, 'rcc-confirm-button')
    # Локатор для вопроса в раскрывающемся списке
    QUESTION_DROP_DOWN_LIST = (By.ID, 'accordion__heading-{}')
    # Локатор для ответа в раскрывающемся списке
    ANSWER_DROP_DOWN_LIST = (By.ID, 'accordion__panel-{}')
    # Локатор надписи "Вопросы о важном"
    TITLE_QUESTION = (By.XPATH, "//*[text()='Вопросы о важном']")
    # Кнопка 'Заказать' в верхнем меню на главной странице сайта
    BUTTON_ORDER_ON_TOP = (By.XPATH, "//*[contains(@class,'Header_Nav')]/*[text()='Заказать']")
    # Кнопка 'Заказать' внизу на главной странице сайта
    BUTTON_ORDER_BELOW = (By.XPATH, "//*[contains(@class,'Home_FinishButton')]/*[text()='Заказать']")
