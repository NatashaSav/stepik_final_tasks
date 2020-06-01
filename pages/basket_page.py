from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_the_basket(self):
        link = self.browser.find_element(*BasketPageLocators.BUTTON_GO_TO_BASKET)
        link.click()

    def basket_should_not_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), \
            "basket has items"

    def basket_should_be_empty(self):
        text_message = self.browser.find_element_by_css_selector(".content").text
        assert "Your basket is empty" in text_message, "Basket is not empty"