import pytest
import allure
from pages.debit_form_page import DebitFormPage


@allure.feature("Payment by debit card")
@allure.title("Попытка оплаты с некорректными значениями")
@allure.story("Проверка валидации года")
@allure.description("""
Тест проверяет оплату с некорректными данными поля 'год'
1. Переход на страницу приложения
2. Нажатие кнопки 'Купить'
3. Ввод невалидных данных в поле год ('00','2', '')
4. Ввод валидных данных в остальные поля (карта: 1111 2222 3333 4444, месяц: 06, владелец: ivan ivanov, cvc: 123)
5. Нажатие кнопки 'Продолжить'
6. Проверка появления сообщения об ошибке
""")
@pytest.mark.parametrize("year_number, expected_error", [
    ('00', 'Истёк срок действия карты'),
    ('2', 'Неверный формат'),
    ('', 'Неверный формат')
])

def test_invalid_year_number(page, base_url, year_number, expected_error):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(1111222233334444)
    debit_page.fill_month('06')
    debit_page.fill_year(year_number)
    debit_page.fill_owner('ivan ivanov')
    debit_page.fill_cvc('123')
    debit_page.submit_button()
    text = debit_page.get_year_error()
    print(f"Текст ошибки: '{text}'")
    assert expected_error in text