from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import QUESTION_BUTTONS, ANSWER_TEXTS, COOKIE_BUTTON

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def close_cookie(self):
        cookie_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(COOKIE_BUTTON)
    )
        cookie_button.click()
    
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(COOKIE_BUTTON)
    )    

    def click_question(self, index):
        buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(QUESTION_BUTTONS)
    )
        button = buttons[index]
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(button))
        button.click()

    def get_answer_text(self, index):
        answers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(ANSWER_TEXTS)
        )
        return answers[index].text