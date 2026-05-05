from locators import (
    ORDER_BUTTON_TOP, NAME_FIELD, SURNAME_FIELD, ADDRESS_FIELD,
    METRO_STATION, PHONE_FIELD, NEXT_BUTTON, DATE_FIELD,
    RENTAL_PERIOD, COLOR_BLACK, ORDER_FINAL_BUTTON, CONFIRM_BUTTON, SUCCESS_MESSAGE, ORDER_BUTTON_BOTTOM
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):
    @allure.step("Нажать на кнопку Заказать вверху/внизу страницы")
    def click_order_button(self, top=True):
        locator = ORDER_BUTTON_TOP if top else ORDER_BUTTON_BOTTOM
        self.click_element(locator)

    @allure.step("Заполнить поле Имя")
    def set_name(self, name):
        self.find_element(NAME_FIELD).send_keys(name)

    @allure.step("Заполнить поле фамилия")
    def set_surname(self, surname):
        self.find_element(SURNAME_FIELD).send_keys(surname)

    @allure.step("Заполнить поле адрес")
    def set_address(self, address):
        self.find_element(ADDRESS_FIELD).send_keys(address)

    @allure.step("Выбор станции")
    def set_metro_station(self, station):
        metro_input = self.find_element(METRO_STATION)
        metro_input.click()
        station_locator = (By.XPATH, f"//div[text()='{station}']")
        self.wait_for_element_clickable(station_locator).click()

    @allure.step("Заполнить поле телефон")
    def set_phone(self, phone):
        self.find_element(PHONE_FIELD).send_keys(phone)

    @allure.step("Нажатие на кнопку далее")
    def click_next(self):
        self.click_element(NEXT_BUTTON)

    @allure.step("Выбор даты")
    def set_date(self, date):
        date_field = self.find_element(DATE_FIELD)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

    @allure.step("Выбор периода аренды")
    def set_rental_period(self, period):
        self.click_element(RENTAL_PERIOD)
        period_option = (By.XPATH, f"//div[text()='{period}']")
        self.wait_for_element_clickable(period_option).click()

    @allure.step("Выбор цвета")
    def select_color_black(self):
        self.click_element(COLOR_BLACK)

    @allure.step("Нажатие кнопки заказать на форме «Про аренду»")
    def click_order_final(self):
        self.click_element(ORDER_FINAL_BUTTON)

    @allure.step("Нажатие кнопки подтверждения заказа Да")
    def confirm_order(self):
        self.click_element(CONFIRM_BUTTON)

    @allure.step("Получить сообщение о успешном заказе")
    def get_success_message(self):
        return self.wait_for_text_not_empty_in_element(SUCCESS_MESSAGE).text

    @allure.step("Заполнение формы заказа")
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