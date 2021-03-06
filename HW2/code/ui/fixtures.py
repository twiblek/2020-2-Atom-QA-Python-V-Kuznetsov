import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.create_camp_page import CreateCampPage
from ui.pages.campaigns_page import CampaignsPage
from ui.pages.create_segm_page import CreateSegmPage
from ui.pages.segments_page import SegmentsPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def campaigns_page(driver):
    return CampaignsPage(driver=driver)


@pytest.fixture
def create_camp_page(driver):
    return CreateCampPage(driver=driver)


@pytest.fixture
def segments_page(driver):
    return SegmentsPage(driver=driver)


@pytest.fixture
def create_segm_page(driver):
    return CreateSegmPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    download_dir = config['download_dir']
    selenoid = config['selenoid']

    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=800,600")

        if selenoid:
            selenoid_url = 'http://' + selenoid + '/wd/hub'
            driver = webdriver.Remote(command_executor=selenoid_url,
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True}
                                      )

        else:

            prefs = {"download.default_directory": download_dir}
            options.add_experimental_option('prefs', prefs)

            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install(),
                                       options=options,
                                       desired_capabilities={'acceptInsecureCerts': True}
                                       )


    elif browser == 'firefox':
        manager = GeckoDriverManager(version=version)
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver

    # quit = закрыть страницу, остановить browser driver
    # close = закрыть страницу, бинарь browser driver останется запущенным
    driver.quit()