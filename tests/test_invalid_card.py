import pytest
import allure
from pages.debit_form_page import DebitFormPage

@allure.feature("Payment by debit card")
@allure.title("Попытка оплаты с некорректными значениями")
@allure.story("Проверка валидации номера карты")
@allure.description("""
Тест проверяет оплату с некорректными данными поля 'Номер карты'
1. Переход на страницу приложения
2. Нажатие кнопки 'Купить'
3. Ввод невалидных данных в поле 'Номер карты' (15 цифр или пустая строка)
4. Ввод валидных данных в остальные поля (формируются динамически)
5. Нажатие кнопки 'Продолжить'
6. Проверка появления сообщения об ошибке
""")
@pytest.mark.parametrize(
    "card_number",
    ['123456789012345',
     ''])
def test_invalid_card_number(page, base_url, card_number, valid_month, valid_year, valid_owner, valid_cvc):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(card_number)
    debit_page.fill_month(valid_month)
    debit_page.fill_year(valid_year)
    debit_page.fill_owner(valid_owner)
    debit_page.fill_cvc(valid_cvc)
    debit_page.submit_button()
    text = debit_page.get_card_number_error()
    print(f"Текст ошибки: '{text}'")
    assert "Неверный формат" in text
