from .base_page import BasePage
from .locators import ProductPageLocators
import pytest

class ProductPage(BasePage):
    def go_button_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()

    @pytest.mark.xfail
    def message_product_should_be_add_to_the_basket(self):
        name_current_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        actual_message = self.browser.find_element(*ProductPageLocators.ACTUAL_MESSAGE).text
        expect_message = name_current_book + ' has been added to your basket.'
        assert actual_message in expect_message, "Name book in message not found"
        # pytest -rx -v unit/fixut/test_product_page.py

    def message_with_cost_basket(self):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_basket == price_product, "prices is different"

    # def should_be_success_message(self):
    #     assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
    #         "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
             "Success message is not disappeared, but should not be"
