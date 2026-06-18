import pytest
from selenium import webdriver


@pytest.fixture
def page():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return 'http://localhost:8080'

