import pytest
import allure
from pages.debit_form_page import DebitFormPage

@allure.feature("Payment by debit card")
@allure.title("Попытка оплаты с некорректными значениями")
@allure.story("Проверка валидации владельца")
@allure.description("""
Тест проверяет оплату с некорректными данными поля 'владелец'
1. Переход на страницу приложения
2. Нажатие кнопки 'Купить'
3. Ввод невалидных данных в поле владелец ('', '    ')
4. Ввод валидных данных в остальные поля (карта: 1111 2222 3333 4444, месяц: 06, год: 27, cvc: 123)
5. Нажатие кнопки 'Продолжить'
6. Проверка появления сообщения об ошибке
""")
@pytest.mark.parametrize("owner, expected_error", [
    ('', 'Поле обязательно для заполнения'),
    ('     ', 'Поле обязательно для заполнения'),

])
def test_invalid_owner(page, base_url, owner, expected_error):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(1111222233334444)
    debit_page.fill_month('06')
    debit_page.fill_year('27')
    debit_page.fill_owner(owner)
    debit_page.fill_cvc('123')
    debit_page.submit_button()
    text = debit_page.get_owner_error()
    print(f"Текст ошибки: '{text}'")
    assert expected_error in text
