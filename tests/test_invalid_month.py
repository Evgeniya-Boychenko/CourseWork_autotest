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
4. Ввод валидных данных в остальные поля (год генерируется через datetime, владелец и смс - через Facker)
5. Нажатие кнопки 'Продолжить'
6. Проверка появления сообщения об ошибке
""")
@pytest.mark.parametrize("month_number, expected_error", [
    ('13', 'Неверно указан срок действия карты'),
    ('1', 'Неверный формат'),
    ('', 'Неверный формат')
])
def test_invalid_month_number(page, base_url, month_number, valid_card, valid_year, valid_owner, valid_cvc, expected_error):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(valid_card)
    debit_page.fill_month(month_number)
    debit_page.fill_year(valid_year)
    debit_page.fill_owner(valid_owner)
    debit_page.fill_cvc(valid_cvc)
    debit_page.submit_button()
    text = debit_page.get_month_error()
    print(f"Текст ошибки: '{text}'")
    assert expected_error in text