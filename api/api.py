import logging

import allure
import requests
from allure_commons.types import AttachmentType
from selene import browser
from selene.core.query import value

API_URL = "https://demowebshop.tricentis.com/"


def add_product(product_id, quantity):
    response = requests.post(
        url=f"{API_URL}addproducttocart/catalog/{product_id}/1/{quantity}"
    )
    assert response.status_code == 200

    allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
    logging.info(f'With payload {response.request.body}')
    logging.info(f'Finished with status code {response.status_code}')

    return response


def remove_product():
    item_value = browser.element("[name='removefromcart'").get(value)
    payload = {f"removefromcart": {item_value},
               "updatecart": 'Update shopping cart',
               "discountcouponcode": '',
               "giftcardcouponcode": '',
               }
    response = requests.post(API_URL + "cart", data=payload)

    assert response.status_code == 200

    allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
    logging.info(f'With payload {response.request.body}')
    logging.info(f'Finished with status code {response.status_code}')

    return response
