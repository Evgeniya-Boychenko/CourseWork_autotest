import pytest
from selenium import webdriver
from faker import Faker
from datetime import datetime

from helpers.data_helper import DataHelper


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
    return DataHelper.generate_valid_month()

@pytest.fixture
def valid_year():
    """Возвращает год в формате последних 2 цифр"""
    return DataHelper.generate_valid_year()

@pytest.fixture
def valid_owner():
    """Возвращает случайное валидное имя владельца латиницей"""
    return DataHelper.generate_valid_owner()

@pytest.fixture
def valid_cvc():
    """Возвращает случайный CVC (3 цифры)"""
    return DataHelper.generate_valid_cvc()


@pytest.fixture
def valid_card():
    """Возвращает валидный номер карты"""
    return DataHelper.generate_valid_card()

@pytest.fixture
def invalid_card():
    """Возвращает невалидный номер карты"""
    return DataHelper.generate_invalid_card()

@pytest.fixture
def owner_long():
    """Возвращает длинное имя владельца"""
    return DataHelper.generate_long_owner()


