import allure
import pytest
from selene import browser

from api.api import add_product

WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


@pytest.fixture(scope='function')
def add_product_and_open_browser():
    def _add_product_and_open_browser(product_id, quantity):
        with allure.step("Отправка запроса для добавления товара в корзину"):
            response = add_product(API_URL, product_id, quantity)

        with allure.step("Получаем куки добавления товара в корзину"):
            cookie = response.cookies.get('Nop.customer')

        with allure.step("Открытие страницы корзины и добавление куки"):
            browser.open('https://demowebshop.tricentis.com/')
            browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})

    return _add_product_and_open_browser
