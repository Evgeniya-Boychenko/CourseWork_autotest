import pytest
import allure
from pages.debit_form_page import DebitFormPage

@allure.feature("Payment by debit card")
@allure.title("Попытка оплаты с некорректными значениями")
@allure.story("Проверка валидации месяца")
@allure.description("""
Тест проверяет оплату с некорректными данными поля 'месяц'
1. Переход на страницу приложения
2. Нажатие кнопки 'Купить'
3. Ввод невалидных данных в поле месяц ('13','1', '')
4. Ввод валидных данных в остальные поля (карта: 1111 2222 3333 4444, год: 27, владелец: ivan ivanov, cvc: 123)
5. Нажатие кнопки 'Продолжить'
6. Проверка появления сообщения об ошибке
""")
@pytest.mark.parametrize("month_number, expected_error", [
    ('13', 'Неверно указан срок действия карты'),
    ('1', 'Неверный формат'),
    ('', 'Неверный формат')
])
def test_invalid_month_number(page, base_url, month_number, expected_error):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(1111222233334444)
    debit_page.fill_month(month_number)
    debit_page.fill_year('27')
    debit_page.fill_owner('ivan ivanov')
    debit_page.fill_cvc('123')
    debit_page.submit_button()
    text = debit_page.get_month_error()
    print(f"Текст ошибки: '{text}'")
    assert expected_error in text