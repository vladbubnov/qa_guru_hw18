import allure
import pytest

import data
from api.api import remove_product
from data.product import book_1, book_2, book_3

from pages.cart_page import check_added_product
from pages.main_page import click_shopping_cart_button
from tests.conftest import API_URL


@allure.title("Добавление разного количества товара в корзину")
@pytest.mark.parametrize("product_id, product_name, quantity", [
    (book_1.id, book_1.name, book_1.quantity),
    (book_2.id, book_2.name, book_2.quantity),
    (book_3.id, book_3.name, book_3.quantity)
])
def test_add_to_cart(add_product_and_open_browser, product_id, product_name, quantity):
    with allure.step("Добавляем товар в корзину"):
        add_product_and_open_browser(product_id, quantity)

    with allure.step("Переход в корзину"):
        click_shopping_cart_button()

    with allure.step("Проверяем добавленный товар"):
        check_added_product(quantity, product_name)


def test_remove_from_cart(add_product_and_open_browser):
    with allure.step("Добавляем товар в корзину"):
        add_product_and_open_browser(book_1.id, book_1.quantity)

    with allure.step("Переход в корзину"):
        click_shopping_cart_button()

    with allure.step("Удаляем товар из корзины"):
        remove_product(API_URL)

    with allure.step("Проверяем пустую корзину"):
        click_shopping_cart_button()
