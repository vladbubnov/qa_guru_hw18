from selene import browser, by, be


def click_shopping_cart_button():
    browser.element(by.text("Shopping cart")).click()
    browser.element(".page-title").should(be.visible)

