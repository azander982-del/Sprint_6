import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGO_MAIN, YANDEX_LOGO

def test_scooter_logo(driver):
    driver.get("https://qa-scooter.praktikum-services.ru/order")
    logo = driver.find_element(*LOGO_MAIN)
    logo.click()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

def test_yandex_logo(driver):
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yandex_logo = driver.find_element(*YANDEX_LOGO)
    yandex_logo.click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 15).until(EC.url_contains("dzen.ru"))
    assert "dzen.ru" in driver.current_url