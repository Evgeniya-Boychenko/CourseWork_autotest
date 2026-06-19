import pytest
from selenium import webdriver
from faker import Faker
from datetime import datetime


@pytest.fixture
def page():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return 'http://localhost:8080'

@pytest.fixture
def valid_month():
    """Возвращает текущий месяц в формате 2 цифр"""
    return str(datetime.now().month).zfill(2)

@pytest.fixture
def valid_year():
    """Возвращает год в формате последних 2 цифр"""
    return str(datetime.now().year)[-2:]

fake = Faker()
@pytest.fixture
def valid_owner():
    """Возвращает случайное валидное имя владельца латиницей"""
    return f"{fake.first_name()} {fake.last_name()}"

@pytest.fixture
def valid_cvc():
    """Возвращает случайный CVC (3 цифры)"""
    return fake.credit_card_security_code()


@pytest.fixture
def valid_card():
    """Возвращает валидный номер карты"""
    return "1111222233334444"

@pytest.fixture
def invalid_card():
    """Возвращает невалидный номер карты"""
    return "5555666677778888"

@pytest.fixture
def owner_long():
    """Возвращает длинное имя владельца"""
    return 'ivan ivanov' * 10


