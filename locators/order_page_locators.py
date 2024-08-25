from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Поле ввода имени для заказа
    FIELD_NAME = (By.XPATH, "//*[@placeholder='* Имя']/../input")
    # Поле ввода фамилии для заказа
    FIELD_SURNAME = (By.XPATH, "//*[@placeholder='* Фамилия']/../input")
    # Поле ввода адреса для заказа
    FIELD_ADDRESS = (By.XPATH, "//*[@placeholder='* Адрес: куда привезти заказ']/../input")
    # Поле ввода станции метро
    FIELD_UNDERGROUND = (By.XPATH, "//*[@placeholder='* Станция метро']/../input")
    # Поле ввода номера телефона
    FIELD_PHONE = (By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']/../input")
    # Станция метро 'Черкизовская' в списке станций
    STATION_METRO = (By.XPATH, "//*[text()='Сокольники']")
    # Заголовок 'Для кого самокат' на странице заказа
    TITLE_ORDER = (By.XPATH, "//*[text()='Для кого самокат']")
    # Кнопка Далее странице заказа
    BUTTON_NEXT = (By.XPATH, "//*[contains(@class,'Button_Middle__')][text()='Далее']")
    # Заголовок 'Про аренду' на странице заказа
    TITLE_ABOUT_RENT = (By.XPATH, "//*[text()='Про аренду']")
    # Поле ввода "Когда привезти самокат"
    FIELD_DATE = (By.XPATH, "//*[@placeholder='* Когда привезти самокат']/../input")
    # Поле выпадающего списка срока аренды
    FIELD_RENTAL_PERIOD = (By.XPATH, "//*[text()='* Срок аренды']")
    # Вариант 'двое суток' в списке срока аренды
    RENT_DAY = (By.XPATH, "//*[@class = 'Dropdown-option' and text()='сутки']")
    # Кнопка "Заказать" для оформления заказа
    BUTTON_ORDER = (By.XPATH, "//*[contains(@class,'Button_Middle__')][text()='Заказать']")
    # Модальное окно подтверждения заказа
    MODAL_CHECKOUT = (By.XPATH, "//*[contains(@class,'Order_ModalHeader__')]")
    # Кнопка 'Да' в модальном окне подтверждения заказа
    BUTTON_YES_CHECKOUT = (By.XPATH, "//button[text()='Да']")
    # Надпись об успешном оформлении заказа
    TITLE_ORDER_SUCCESS = (By.XPATH, "//*[contains(@class,'Order_ModalHeader__')]")
    # Кнопка 'Посмотреть статус' в окне успешно оформленного заказа
    BUTTON_SEE_STATUS = (By.XPATH, "//*[contains(@class,'Button_Middle__')][text()='Посмотреть статус']")