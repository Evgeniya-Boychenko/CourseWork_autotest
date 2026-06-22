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
3. Ввод валидных данных в поля (формируются динамически)
4. Нажатие кнопки 'Продолжить'
5. Проверка появления сообщения "Успешно" (валидация не сработала)
""")
def test_invalid_owner_name_bug(page, base_url, valid_card, valid_month, valid_year, owner_long, valid_cvc):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(valid_card)
    debit_page.fill_month(valid_month)
    debit_page.fill_year(valid_year)
    debit_page.fill_owner(owner_long)
    debit_page.fill_cvc(valid_cvc)
    debit_page.submit_button()
    notification_text = debit_page.get_full_notification_text()
    assert "Операция одобрена" in notification_text
