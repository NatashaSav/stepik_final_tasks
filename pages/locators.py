from selenium.webdriver.common.by import By


class MainPageLocators():
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