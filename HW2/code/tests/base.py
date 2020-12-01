import os

import pytest
from _pytest.fixtures import FixtureRequest

from ui.decorators import wait
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.create_camp_page import CreateCampPage
from ui.pages.campaigns_page import CampaignsPage
from ui.pages.create_segm_page import CreateSegmPage
from ui.pages.segments_page import SegmentsPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.create_camp_page: CreateCampPage = request.getfixturevalue('create_camp_page')
        self.campaigns_page: CampaignsPage = request.getfixturevalue('campaigns_page')        
        self.create_segm_page: CreateSegmPage = request.getfixturevalue('create_segm_page')
        self.segments_page: SegmentsPage = request.getfixturevalue('segments_page')