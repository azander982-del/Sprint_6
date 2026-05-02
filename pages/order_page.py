from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    ORDER_BUTTON_TOP, NAME_FIELD, SURNAME_FIELD, ADDRESS_FIELD,
    METRO_STATION, PHONE_FIELD, NEXT_BUTTON, DATE_FIELD,
    RENTAL_PERIOD, COLOR_BLACK, ORDER_FINAL_BUTTON, CONFIRM_BUTTON, SUCCESS_MESSAGE,YANDEX_LOGO ,LOGO_MAIN, ORDER_BUTTON_BOTTOM
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def click_order_button(self, top=True):
        button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(ORDER_BUTTON_TOP if top else ORDER_BUTTON_BOTTOM)
    )
        button.click()

    def set_name(self, name):
        self.driver.find_element(*NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*ADDRESS_FIELD).send_keys(address)

    def set_metro_station(self, station):
        metro_input = self.driver.find_element(*METRO_STATION)
        metro_input.click()
        station_locator = (By.XPATH, f"//div[text()='{station}']")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(station_locator)
        ).click()

    def set_phone(self, phone):
        self.driver.find_element(*PHONE_FIELD).send_keys(phone)

    def click_next(self):
        self.driver.find_element(*NEXT_BUTTON).click()

    def set_date(self, date):
        date_field = self.driver.find_element(*DATE_FIELD)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

    def set_rental_period(self, period):
        self.driver.find_element(*RENTAL_PERIOD).click()
        period_option = (By.XPATH, f"//div[text()='{period}']")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(period_option)
        ).click()

    def select_color_black(self):
        self.driver.find_element(*COLOR_BLACK).click()

    def click_order_final(self):
        self.driver.find_element(*ORDER_FINAL_BUTTON).click()

    def confirm_order(self):
        confirm_btn = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(CONFIRM_BUTTON)
    )
        confirm_btn.click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SUCCESS_MESSAGE)
        ).text

    def create_order(self, order_data, top=True):
        self.click_order_button(top)
        self.set_name(order_data["name"])
        self.set_surname(order_data["surname"])
        self.set_address(order_data["address"])
        self.set_metro_station(order_data["metro_station"])
        self.set_phone(order_data["phone"])
        self.click_next()
        self.set_date(order_data["date"])
        self.set_rental_period(order_data["rental_period"])
        self.select_color_black()
        self.click_order_final()
        self.confirm_order()
        return self.get_success_message()

    def test_scooter_logo(driver):
        driver.get("https://qa-scooter.praktikum-services.ru/order")  # уходим с главной
        logo = driver.find_element(*LOGO_MAIN)
        logo.click()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
    
    def test_yandex_logo(driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        yandex_logo = driver.find_element(*YANDEX_LOGO)
        yandex_logo.click()
        WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        assert "dzen.ru" in driver.current_url

        driver.close()