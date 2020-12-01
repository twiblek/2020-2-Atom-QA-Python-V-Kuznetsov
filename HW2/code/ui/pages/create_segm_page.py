from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import CreateSegmentLocators
from ui.pages.base_page import BasePage

import time


class CreateSegmPage(BasePage):
    locators = CreateSegmentLocators()

    def creation(self):

        self.click(self.locators.SEGMENT_CHECKBOX)
        self.click(self.locators.ADD_SEGMENT_BUTTON)

        segment_name = self.find(self.locators.SEGMENT_NAME).get_attribute('value')

        self.click(self.locators.CREATE_BUTTON)

        return segment_name