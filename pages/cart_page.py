from selene import have, browser


def check_added_product(count_product, product_name):
    browser.all(".cart-item-row").should(have.size(1))
    browser.element(".product-name").should(have.text(product_name))
    browser.element(".qty-input").should(have.attribute(name="value", value=count_product))


def update_cookies(browser_management, cookie):
    browser_management.driver.add_cookie({"name": "Nop.customer", "value": cookie})
    browser.driver.refresh()


def check_removed_product():
    browser.element("[class='page shopping-cart-page'").should(have.text("Your Shopping Cart is empty"))
