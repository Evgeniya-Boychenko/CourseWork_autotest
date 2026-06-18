import pytest
import allure
from pages.debit_form_page import DebitFormPage

@allure.feature("Payment by debit card")
@allure.title("Попытка оплаты с некорректными значениями")
@allure.story("Проверка валидации cvc,cvv")
@allure.description("""
Тест проверяет оплату с некорректными данными поля 'cvc/cvv'
1. Переход на страницу приложения
2. Нажатие кнопки 'Купить'
3. Ввод невалидных данных в поле cvc ('','1', '12')
4. Ввод валидных данных в остальные поля (карта: 1111 2222 3333 4444, месяц: 06, год: 27, владелец: ivan ivanov)
5. Нажатие кнопки 'Продолжить'
6. Проверка появления сообщения об ошибке
""")
@pytest.mark.parametrize("cvc, expected_error", [
    ('', 'Неверный формат'),
    ('1', 'Неверный формат'),
    ('12', 'Неверный формат')

])
def test_invalid_cvc(page, base_url, cvc, expected_error):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(1111222233334444)
    debit_page.fill_month('06')
    debit_page.fill_year('27')
    debit_page.fill_owner('ivan ivanov')
    debit_page.fill_cvc(cvc)
    debit_page.submit_button()
    text = debit_page.get_cvc_error()
    print(f"Текст ошибки: '{text}'")
    assert expected_error in text
