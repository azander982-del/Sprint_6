import pytest
import allure
from pages.order_page import OrderPage

order_data_set1 = {
    "name": "Иван",
    "surname": "Петров",
    "address": "ул. Ленина, 10",
    "metro_station": "Черкизовская",
    "phone": "+79998887766",
    "date": "05.06.2026",
    "rental_period": "двое суток"
}

order_data_set2 = {
    "name": "Анна",
    "surname": "Сидорова",
    "address": "ул. Гагарина, 5",
    "metro_station": "Преображенская площадь",
    "phone": "+79115556677",
    "date": "10.06.2026",
    "rental_period": "четверо суток"
}

@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Проверка успешного заказа через разные кнопки")
    @pytest.mark.parametrize("order_data, use_top_button", [
        (order_data_set1, True),
        (order_data_set2, False)
    ])
    def test_successful_order(self, driver, order_data, use_top_button):
        order_page = OrderPage(driver)
        success_text = order_page.create_order(order_data, top=use_top_button)
        assert "Заказ оформлен" in success_text