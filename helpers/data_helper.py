from datetime import datetime
from faker import Faker

class DataHelper:
    """Класс для генерации тестовых данных"""

    @staticmethod
    def generate_valid_month():
        """Возвращает текущий месяц в формате 2 цифр"""
        return str(datetime.now().month).zfill(2)

    @staticmethod
    def generate_valid_year():
        """Возвращает год в формате последних 2 цифр"""
        return str(datetime.now().year)[-2:]

    @staticmethod
    def generate_valid_owner():
        """Возвращает случайное валидное имя владельца латиницей"""
        fake = Faker()
        return f"{fake.first_name()} {fake.last_name()}"

    @staticmethod
    def generate_valid_cvc():
        """Возвращает случайный CVC (3 цифры)"""
        fake = Faker()
        return fake.credit_card_security_code()

    @staticmethod
    def generate_valid_card():
        """Возвращает валидный номер карты"""
        return "1111222233334444"

    @staticmethod
    def generate_invalid_card():
        """Возвращает невалидный номер карты"""
        return "5555666677778888"

    @staticmethod
    def generate_long_owner():
        """Возвращает длинное имя владельца"""
        return 'ivan ivanov' * 10