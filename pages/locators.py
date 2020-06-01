from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASSWORD = (By.NAME, "registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.NAME, "registration-password2")
    REGISTER_EMAIL_FOR_USER = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_FOR_USER = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_FOR_USER = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".product_main .btn-add-to-basket")
    PRICE_BASKET = (By.CSS_SELECTOR, "div.alertinner p strong")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    ACTUAL_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators:
    BUTTON_GO_TO_BASKET = (By.CLASS_NAME, "btn-group")
    BASKET_FORMSET = (By.ID, "basket_formset")
