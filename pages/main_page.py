from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


# код использовался до того момента, пока не была поставлена заглушка. Тема "Плюсы наследования: пример"

# def go_to_login_page(self):
#     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "do not go to the login link"
#
# def should_be_login_link(self):
#     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
#
# def go_to_login_page(self):
#     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#     link.click()
