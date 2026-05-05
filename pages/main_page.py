from locators import QUESTION_BUTTONS, ANSWER_TEXTS, COOKIE_BUTTON, LOGO_MAIN, YANDEX_LOGO
from pages.base_page import BasePage
import allure
import time

class MainPage(BasePage):
    @allure.step("Закрыть куки")
    def close_cookie(self):
        self.click_element(COOKIE_BUTTON)
        self.wait_element_invisible(COOKIE_BUTTON)

    @allure.step("Нажать на вопрос")
    def click_question(self, index):
        buttons = self.wait_for_all_elements(QUESTION_BUTTONS)
        button = buttons[index]
        self.scroll_to_element(button)
        time.sleep(0.5) # понимаю, что использовать слип это моветон, но никак не могу понять, как без него. 3 разных варианта пробовал - всё равно падает тест(нейронка говорит надо JS юзать - такого в теории не было, а вот слип был)
        button.click()
        self.wait_for_text_not_empty(ANSWER_TEXTS, index)
    @allure.step("Получить ответ на вопрос")
    def get_answer_text(self, index):
        answers = self.wait_for_all_elements(ANSWER_TEXTS)
        return answers[index].text

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(LOGO_MAIN)

    @allure.step("Кликнуть на логотип Яндекса и переключиться на вкладку Дзен")
    def click_yandex_logo_and_switch_to_dzen(self):
        self.click_element(YANDEX_LOGO)
        self.wait_for_new_window(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_for_url_contains("dzen.ru")

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url