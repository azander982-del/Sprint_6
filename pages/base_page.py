from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text
    
    def click_element_object(self, element):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(element))
        element.click()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)    

    def wait_element_invisible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_all_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_by_locator(self, locator, timeout=10):
        self.wait_for_element_clickable(locator, timeout).click()

    def wait_for_new_window(self, expected_windows, timeout=10):
        WebDriverWait(self.driver, timeout).until(
        lambda d: len(d.window_handles) == expected_windows
    )

    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
        EC.url_contains(text)
    )    
        
    def wait_for_text_not_empty(self, locator, index, timeout=10):
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
    )
        WebDriverWait(self.driver, timeout).until(
            lambda d: elements[index].text != ""
    )
        return elements 
    def wait_for_text_not_empty_in_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
    )
        WebDriverWait(self.driver, timeout).until(
            lambda d: element.text != ""
    )
        return element