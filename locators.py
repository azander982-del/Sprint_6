from selenium.webdriver.common.by import By


QUESTION_BUTTONS = (By.XPATH, "//div[contains(@class, 'accordion__button')]")  #кнопка меню вопросов
ANSWER_TEXTS = (By.XPATH, "//div[contains(@class, 'accordion__panel')]/p")  # текст ответа на вопрос
COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']") # кнопка да все уже привыкли
ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")  #  верхняя кнопка заказать
ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']") #  нижняя кнопка заказать
NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")  # поле имя
SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']") # поле фамилия
ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  #поле адрес
METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']") # поле станция метро
PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # поле телефон
NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")  # кнопка далее на форме заказа
DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # поле когда привезти самакат на форме "Про аренду"
RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")  # поле Срок аренды на форме "Про аренду"
COLOR_BLACK = (By.XPATH, "//input[@id='black']") # выбор черного цвета на форме "Про аренду"
ORDER_FINAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Заказать']")  #нижняя кнопка "Заказать"
CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")  # Кнопка да на форме "Хотите оформить заказ?"
SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")  # Форма "Заказ оформлен"
LOGO_MAIN = (By.XPATH, "//a[@href='/']")  # логотип самоката
YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")  # логотип яндекса