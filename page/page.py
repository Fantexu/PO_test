from page.homePage import HomePage
from page.loginPage import LoginPage


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def home_page(self):
        return HomePage(self.driver)

    @property
    def login_page(self):
        return LoginPage(self.driver)