import pytest
import pymysql
import time
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
@allure.title("Попытка оплаты с корректными значениями")
@allure.story ("Проверка ответа банка (APPROVED)")
@allure.description("""
Тест проверяет оплату с корректными данными 
1. Переход на страницу приложения
2. Нажатие кнопки 'Купить'
3. Ввод валидных данных в поля (карта: 1111 2222 3333 4444, месяц: 06, год: 27, владелец: ivan ivanov, cvc: 123)
4. Нажатие кнопки 'Продолжить'
5. Проверка появления сообщения успешной операции
""")
@pytest.mark.parametrize("card_number, month_number, year_number, owner, cvc, expected_status", [
    ("1111 2222 3333 4444", "06", "27", "ivan ivanov", "123", "APPROVED")
    ])
def test_approve_card_with_db_check(page, base_url, card_number, month_number, year_number, owner, cvc, expected_status):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(card_number)
    debit_page.fill_month(month_number)
    debit_page.fill_year(year_number)
    debit_page.fill_owner(owner)
    debit_page.fill_cvc(cvc)
    debit_page.submit_button()
    debit_page.wait_for_notification()
    notification_text = debit_page.get_full_notification_text()

    is_approved = (expected_status == "APPROVED")

    if is_approved:
        assert "Успешно" in notification_text
    else:
        assert "Ошибка" in notification_text

    time.sleep(2)

    db_status = get_last_payment_status()
    assert db_status == expected_status

@allure.feature("Payment by debit card")
@allure.title("Попытка оплаты с номером карты, который должен быть отклонен")
@allure.story("Проверка ответа банка (DECLINED)")
@allure.description("""
Тест проверяет оплату с данными карты, которые должны быть отклонены 
1. Переход на страницу приложения
2. Нажатие кнопки 'Купить'
3. Ввод номера карты, который заведомо должен быть отклонен ('5555 6666 7777 8888')
4. Ввод валидных данных в остальные поля (месяц: 06, год: 27, владелец: ivan ivanov, cvc: 123)
5. Нажатие кнопки 'Продолжить'
6. Проверка появления сообщения об ошибке
""")
@pytest.mark.xfail(reason="Баг №6: симулятор банка одобряет DECLINED карту")
@pytest.mark.parametrize("card_number, month_number, year_number, owner, cvc, expected_status", [
    ("5555 6666 7777 8888", "06", "27", "ivan ivanov", "123", "DECLINED")
    ])
def test_decline_card_with_db_check(page, base_url, card_number, month_number, year_number, owner, cvc,
                                        expected_status):
    page.get(base_url)
    debit_page = DebitFormPage(page)
    debit_page.click_buy_button()
    debit_page.fill_card_number(card_number)
    debit_page.fill_month(month_number)
    debit_page.fill_year(year_number)
    debit_page.fill_owner(owner)
    debit_page.fill_cvc(cvc)
    debit_page.submit_button()
    debit_page.wait_for_notification()
    notification_text = debit_page.get_full_notification_text()

    is_approved = (expected_status == "APPROVED")

    if is_approved:
            assert "Успешно" in notification_text
    else:
            assert "Ошибка"  in notification_text

    time.sleep(2)

    db_status = get_last_payment_status()
    assert db_status == expected_status

