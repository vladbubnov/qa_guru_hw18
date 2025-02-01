import allure
import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_management():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open('https://demowebshop.tricentis.com/')
    yield browser
    browser.quit()

