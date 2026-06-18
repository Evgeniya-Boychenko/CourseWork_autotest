import pytest
import allure
from pages.debit_form_page import DebitFormPage

@allure.feature("Payment by debit card")
@allure.title("Попытка оплаты с длинным именем владельца (100+ символов)")
@allure.story("Проверка валидации владельца")
@allure.description("""
Тест проверяет оплату с некорректным данным поля 'владелец' (100+ символов)
1. Переход на страницу приложения
2. Нажатие кнопки 'Купить'
3. Ввод невалидных данных в поле владелец ('ivan ivanov' * 10)
4. Ввод валидных данных в остальные поля (карта: 1111 2222 3333 4444, месяц: 06, год: 27, cvc: 123)
5. Нажатие кнопки 'Продолжить'
6. Проверка появления сообщения "Успешно" (валидация не сработала)
""")
@pytest.mark.parametrize("owner_long, expected_text", [
    ('ivan ivanov ' * 10, "Успешно"),
    ])
def test_invalid_owner_name_bug(page, base_url, owner_long, expected_text):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number('1111222233334444')
    debit_page.fill_month('06')
    debit_page.fill_year('27')
    debit_page.fill_owner(owner_long)
    debit_page.fill_cvc('123')
    debit_page.submit_button()
    debit_page.wait_for_notification()

    notification_text = debit_page.get_full_notification_text()
    assert expected_text in notification_text
