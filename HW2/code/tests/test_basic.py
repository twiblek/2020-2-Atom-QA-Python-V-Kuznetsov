import pytest

from tests.base import BaseCase
from os import path

class Test(BaseCase):

    @pytest.fixture(scope='function')
    def create_segment(self):
        self.base_page.click(self.base_page.locators.SEGMENTS_BUTTON)
        self.segments_page.start_creation()
        name = self.create_segm_page.creation()
        yield name

    @pytest.fixture(scope='function')
    def auth(self):
        self.main_page.click(self.main_page.locators.AUTH_BUTTON)

        login_field = self.main_page.find(self.main_page.locators.LOGIN)
        login_field.send_keys('twi.lek@yandex.ru')

        password_field = self.main_page.find(self.main_page.locators.PASSWORD)
        password_field.send_keys('123456a')

        self.base_page.click(self.main_page.locators.LOG_IN_BUTTON)

        yield self.main_page

    @pytest.mark.ui
    def test_right_auth(self, auth):
        assert "Рекламная платформа myTarget — Сервис таргетированной рекламы" in self.driver.title

    @pytest.mark.ui
    def test_wrong_auth(self):
        self.main_page.authorization('qwert1@yandex.ru', 'qwer1')
        assert "Invalid login or password" in self.driver.page_source

    @pytest.mark.ui
    def test_create_campaign(self, auth):
        self.campaigns_page.start_creation()

        image_path = path.join(path.dirname(path.abspath(__file__)), 'banner.jpg')

        campaign_name = self.create_camp_page.creation(title = 'title', 
                                                       url = 'https://technoatom.mail.ru/', 
                                                       image_path = image_path)

        self.base_page.find(self.campaigns_page.locators.CAMPAIGNS_TABLE)
        assert campaign_name in self.driver.page_source
    
    @pytest.mark.ui
    def test_create_segment(self, auth, create_segment):
        self.segments_page.find(self.segments_page.locators.SEGMENTS_TABLE)
        assert create_segment in self.driver.page_source

    @pytest.mark.ui
    def test_delete_segment(self, auth, create_segment):
        edited_locator = (self.segments_page.locators.SEGMENT_ROW[0], 
                          self.segments_page.locators.SEGMENT_ROW[1].format(create_segment))

        segment_href = self.segments_page.find(edited_locator).get_attribute('href')
        segment_id = segment_href.split('/')[-1]

        edited_locator = (self.segments_page.locators.DELETE_SEGMENT_CROSS[0], 
                          self.segments_page.locators.DELETE_SEGMENT_CROSS[1].format(segment_id, segment_id))
        self.segments_page.click(edited_locator)

        self.segments_page.click(self.segments_page.locators.CONFIRM_DELETE)
        self.segments_page.count_elements(self.segments_page.locators.CONFIRM_DELETE, 0)
        self.segments_page.find(self.segments_page.locators.SEGMENTS_TABLE)

        assert create_segment not in self.driver.page_source