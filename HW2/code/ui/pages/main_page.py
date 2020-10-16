from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def authorization(self, login = 'twi.lek@yandex.ru', password = '123456a', timeout = 10):
        self.click(self.locators.AUTH_BUTTON, timeout=timeout)

        login_field = self.find(self.locators.LOGIN)
        login_field.send_keys(login)

        password_field = self.find(self.locators.PASSWORD)
        password_field.send_keys(password)

        self.click(self.locators.LOG_IN_BUTTON, timeout=timeout)