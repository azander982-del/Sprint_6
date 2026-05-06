import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Кликнуть по элементу {locator}")
    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text
    
    @allure.step("Кликнуть по элементу")
    def click_element_object(self, element):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)    

    @allure.step("Дождаться невидимости элемента {locator}")
    def wait_element_invisible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Дождаться кликабельности элемента {locator}")
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    @allure.step("Дождаться всех элементов {locator}")
    def wait_for_all_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
    @allure.step("Кликнуть по локатору {locator}")
    def click_by_locator(self, locator, timeout=10):
        self.wait_for_element_clickable(locator, timeout).click()

    @allure.step("Дождаться появления нового окна")
    def wait_for_new_window(self, expected_windows, timeout=10):
        WebDriverWait(self.driver, timeout).until(
        lambda d: len(d.window_handles) == expected_windows
    )
    @allure.step("Дождаться, что URL содержит '{text}'")
    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
        EC.url_contains(text)
    )    
    
    @allure.step("Дождаться, что текст элемента не пустой, индекс {index}")   
    def wait_for_text_not_empty(self, locator, index, timeout=10):
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
    )
        WebDriverWait(self.driver, timeout).until(
            lambda d: elements[index].text != ""
    )
        return elements 
    
    @allure.step("Дождаться, что текст элемента не пустой")
    def wait_for_text_not_empty_in_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
    )
        WebDriverWait(self.driver, timeout).until(
            lambda d: element.text != ""
    )
        return element
    
    @allure.step("Дождаться кликабельности элемента (объект)")
    def wait_for_element_object_to_be_clickable(self, element, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))

    @allure.step("Переключиться на последнюю вкладку")
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])    

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url    
    
    @allure.step("Переключиться на вкладку")
    def switch_to_window_by_index(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])