import pytest
import allure
from pages.debit_form_page import DebitFormPage

@allure.feature("Payment by debit card")
@allure.title("Попытка оплаты с некорректными значениями")
@allure.story("Проверка валидации cvc/cvv")
@allure.description("""
Тест проверяет оплату с некорректными данными поля 'cvc/cvv'
1. Переход на страницу приложения
2. Нажатие кнопки 'Купить'
3. Ввод невалидных данных в поле месяц ('','1', '12')
4. Ввод валидных данных в остальные поля (карта: 1111 2222 3333 4444, месяц: 06, год: 27, владелец: ivan ivanov)
5. Нажатие кнопки 'Продолжить'
6. Проверка появления сообщения об ошибке
""")
@pytest.mark.parametrize(
    "card_number",
    ['123456789012345',
     ''])
def test_invalid_card_number(page, base_url, card_number):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(card_number)
    debit_page.fill_month('06')
    debit_page.fill_year('27')
    debit_page.fill_owner('ivan ivanov')
    debit_page.fill_cvc('123')
    debit_page.submit_button()
    text = debit_page.get_card_number_error()
    print(f"Текст ошибки: '{text}'")
    assert "Неверный формат" in text
