from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import CreateCampLocators
from ui.pages.base_page import BasePage

import time


class CreateCampPage(BasePage):
    locators = CreateCampLocators()

    def creation(self, title = 'title', url = 'https://technoatom.mail.ru/', text = 'text'):

        self.click(self.locators.TRAFFIC_BUTTON)

        url_field = self.find(self.locators.URL_FIELD)
        url_field.send_keys(url)

        self.click(self.locators.TEASER_FORMAT_BUTTON)

        title_field = self.find(self.locators.TITLE_FIELD)
        title_field.send_keys(title)              
        
        text_field = self.find(self.locators.TEXT_FIELD)
        text_field.send_keys(title)     
        
        self.drag_and_drop(self.locators.TEMPLATE_BANNER_IMAGE, self.locators.UPLOAD_BANNER_IMAGE_BUTTON)

        name_campaign = self.find(self.locators.CAMPAIGN_NAME).get_attribute('value')

        self.click(self.locators.CREATE_BUTTON)

        return name_campaign