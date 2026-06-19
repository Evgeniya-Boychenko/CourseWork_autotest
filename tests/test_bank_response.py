import pytest
import pymysql
import allure
from pages.debit_form_page import DebitFormPage


def get_last_payment_status():
    """Подключается к БД и возвращает статус последней операции"""
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='user',
        password='12345',
        database='app'
    )

    try:
        with connection.cursor() as cursor:
            sql = "SELECT status FROM payment_entity ORDER BY created DESC LIMIT 1"
            cursor.execute(sql)
            result = cursor.fetchone()

            if result:
                return result[0]
            return None
    finally:
        connection.close()

@allure.feature("Payment by debit card")
@allure.title("Оплата валидной картой (APPROVED)")
@allure.story ("Проверка ответа банка (APPROVED)")
@allure.description("""
Тест проверяет оплату с корректными данными 
1. Переход на страницу приложения
2. Нажатие кнопки 'Купить'
3. Ввод валидных данных в поля (генерируются динамически).
4. Нажатие кнопки 'Продолжить'
5. Проверка UI-уведомления и статуса БД
""")
def test_approve_card_with_db_check(page, base_url, valid_month, valid_year, valid_owner, valid_cvc, valid_card):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(valid_card)
    debit_page.fill_month(valid_month)
    debit_page.fill_year(valid_year)
    debit_page.fill_owner(valid_owner)
    debit_page.fill_cvc(valid_cvc)
    debit_page.submit_button()
    notification_text = debit_page.get_full_notification_text()
    assert "Успешно" in notification_text
    db_status = get_last_payment_status()
    assert db_status == "APPROVED"

@allure.feature("Payment by debit card")
@allure.title("Оплата картой, которая должна быть отклонена (DECLINED)")
@allure.story("Проверка ответа банка (DECLINED)")
@allure.description("""
Тест проверяет оплату с данными карты, которые должны быть отклонены 
1. Переход на страницу приложения
2. Нажатие кнопки 'Купить'
3. Ввод данных (формируются динамически)
4. Нажатие кнопки 'Продолжить'
5. Проверка появления сообщения об ошибке
""")
@pytest.mark.xfail(reason="Баг: симулятор банка одобряет DECLINED карту")
def test_decline_card_with_db_check(page, base_url, valid_month, valid_year, valid_owner, valid_cvc, invalid_card):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(invalid_card)
    debit_page.fill_month(valid_month)
    debit_page.fill_year(valid_year)
    debit_page.fill_owner(valid_owner)
    debit_page.fill_cvc(valid_cvc)
    debit_page.submit_button()
    notification_text = debit_page.get_full_notification_text()

    assert "Ошибка"  in notification_text

    db_status = get_last_payment_status()
    assert db_status == "DECLINED"

