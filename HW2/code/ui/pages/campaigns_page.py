from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import CampaignsPageLocators
from ui.pages.base_page import BasePage


class CampaignsPage(BasePage):
    locators = CampaignsPageLocators()

    def start_creation(self):
        self.click(self.locators.CREATE_NEW_CAMP_BUTTON)