import allure
import pytest
from selene import browser

from api.api import remove_product, add_product
from data.product import book_1, book_2, book_3
from pages.cart_page import check_added_product, check_removed_product, update_cookies
from pages.main_page import click_shopping_cart_button


@allure.title("Добавление разного количества товара в корзину")
@pytest.mark.parametrize("product_id, product_name, quantity", [
    (book_1.id, book_1.name, book_1.quantity),
    (book_2.id, book_2.name, book_2.quantity),
    (book_3.id, book_3.name, book_3.quantity)
])
def test_add_to_cart(browser_management, product_id, product_name, quantity):
    with allure.step("Добавляем товар в корзину через API"):
        response = add_product(product_id, quantity)
        browser_management.driver.add_cookie({"name": "Nop.customer", "value": response.cookies.get("Nop.customer")})

    with allure.step("Переход в корзину"):
        click_shopping_cart_button()

    with allure.step("Проверяем добавленный товар"):
        check_added_product(quantity, product_name)


def test_remove_from_cart(browser_management):
    with allure.step("Добавляем товар в корзину через API"):
        response_add = add_product(book_1.id, book_1.quantity)
        update_cookies(browser_management, response_add.cookies.get("Nop.customer"))

    with allure.step("Переход в корзину и проверка, что товар добавлен"):
        click_shopping_cart_button()
        check_added_product(book_1.quantity, book_1.name)

    with allure.step("Удаляем товар из корзины"):
        response_remove = remove_product()
        update_cookies(browser_management, response_remove.cookies.get("Nop.customer"))

    with allure.step("Проверяем пустую корзину"):
        check_removed_product()
