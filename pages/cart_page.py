from selene import have, browser


def check_added_product(count_product, product_name):
    browser.element(".product-name").should(have.text(product_name))
    browser.element(".qty-input").should(have.attribute(name="value", value=count_product))


def check_removed_product():
    browser.element("[class='page shopping-cart-page'").should(have.text("Your Shopping Cart is empty!"))
