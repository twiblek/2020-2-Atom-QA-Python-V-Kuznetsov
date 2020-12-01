from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import SegmentsPageLocators
from ui.pages.base_page import BasePage


class SegmentsPage(BasePage):
    locators = SegmentsPageLocators()

    def start_creation(self):
        self.click(self.locators.CREATE_BUTTON)