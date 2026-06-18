from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DebitFormPage:
    """Page Object для формы оплаты дебетовой картой"""

    #Локаторы элементов формы
    BUY_BUTTON = (By.XPATH, "//button[.//span[text()='Купить']]")
    CARD_NUMBER_FIELD = (By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
    MONTH_FIELD = (By.CSS_SELECTOR, "input[placeholder='08']")
    YEAR_FIELD = (By.CSS_SELECTOR, "input[placeholder='22']")
    OWNER_FIELD = (By.XPATH, "(//input[@class='input__control'])[4]")
    CVC_FIELD = (By.CSS_SELECTOR, "input[placeholder='999']")
    SUBMIT_BUTTON = (By.XPATH, "//button[.//span[text()='Продолжить']]")
    NOTIFICATION = (By.CSS_SELECTOR, ".notification")
    NOTIFICATION_TITLE = (By.XPATH, "//div[@class='notification__title']")
    NOTIFICATION_TEXT = (By.CSS_SELECTOR, "div[class='notification__content']")
    CARD_NUMBER_ERROR = (By.XPATH, "//input[@placeholder='0000 0000 0000 0000']/ancestor::span[contains(@class, 'input__inner')]//span[contains(@class, 'input__sub')]")
    MONTH_ERROR = (By.XPATH, "//input[@placeholder='08']/ancestor::span[contains(@class, 'input__inner')]//span[contains(@class, 'input__sub')]")
    YEAR_ERROR = (By.XPATH, "//input[@placeholder='22']/ancestor::span[contains(@class, 'input__inner')]//span[contains(@class, 'input__sub')]")
    OWNER_ERROR = (By.XPATH, "//span[text()='Владелец']/ancestor::span[contains(@class, 'input__inner')]//span[contains(@class, 'input__sub')]")
    CVC_ERROR = (By.XPATH, "//input[@placeholder='999']/ancestor::span[contains(@class, 'input__inner')]//span[contains(@class, 'input__sub')]")

    def __init__(self, driver):
        """Инициализация страницы"""
        self.driver = driver

    def click_buy_button(self):
        """Нажать кнопку 'Купить'"""
        self.driver.find_element(*self.BUY_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CARD_NUMBER_FIELD))

    def fill_card_number(self, card_number):
        """Заполнить поле номера карты"""
        field = self.driver.find_element(*self.CARD_NUMBER_FIELD)
        field.clear()
        field.send_keys(card_number)

    def fill_month(self, month):
        """Заполнить поле месяца"""
        field = self.driver.find_element(*self.MONTH_FIELD)
        field.clear()
        field.send_keys(month)

    def fill_year(self, year):
        """Заполнить поле года"""
        field = self.driver.find_element(*self.YEAR_FIELD)
        field.clear()
        field.send_keys(year)

    def fill_owner(self, owner):
        """Заполнить поле владельца"""
        field = self.driver.find_element(*self.OWNER_FIELD)
        field.clear()
        field.send_keys(owner)

    def fill_cvc(self, cvc):
        """Заполнить поле CVC"""
        field = self.driver.find_element(*self.CVC_FIELD)
        field.clear()
        field.send_keys(cvc)

    def submit_button(self):
        """Нажать кнопку 'Продолжить'"""
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        button.click()

    def wait_for_notification(self):
        """Подождать появления сообщения"""
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.NOTIFICATION)
        )

    def get_full_notification_text(self):
        """Получить весь текст уведомления"""
        notification = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.NOTIFICATION)
        )
        title = notification.find_element(By.CSS_SELECTOR, ".notification__title").text
        content = notification.find_element(By.CSS_SELECTOR, ".notification__content").text
        return f"{title} {content}"

    # def get_notification(self):
    #     """Получить сообщение"""
    #     element =self.driver.find_element(*self.NOTIFICATION)
    #     return element.text
    #
    # def get_notification_title(self):
    #     """Получить заголовок сообщения"""
    #     element = self.driver.find_element(*self.NOTIFICATION_TITLE)
    #     return element.text
    #
    # def get_notification_text(self):
    #     """Получить текст сообщения"""
    #     element = self.driver.find_element(*self.NOTIFICATION_TEXT)
    #     return element.text

    def get_card_number_error(self):
        """Получить текст ошибки под полем номера карты"""
        try:
            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CARD_NUMBER_ERROR)
            )
            error = self.driver.find_element(*self.CARD_NUMBER_ERROR)
            return error.text
        except:
            return ""


    def get_month_error(self):
        """Получить текст ошибки под полем месяца"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.MONTH_ERROR)
            )
            error = self.driver.find_element(*self.MONTH_ERROR)
            return error.text
        except:
            return ""

    def get_year_error(self):
        """Получить текст ошибки под полем года"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.YEAR_ERROR)
            )
            error = self.driver.find_element(*self.YEAR_ERROR)
            return error.text
        except:
            return ""

    def get_owner_error(self):
        """Получить текст ошибки под полем владелец"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.OWNER_ERROR)
            )
            error = self.driver.find_element(*self.OWNER_ERROR)
            return error.text
        except:
            return ""

    def get_cvc_error(self):
        """Получить текст ошибки под полем CVC"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CVC_ERROR)
            )
            error = self.driver.find_element(*self.CVC_ERROR)
            return error.text
        except:
            return ""







