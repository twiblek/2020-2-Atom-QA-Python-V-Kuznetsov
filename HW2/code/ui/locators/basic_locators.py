from selenium.webdriver.common.by import By

class BasePageLocators(object):
    SEGMENTS_BUTTON = (By.XPATH, '//a[contains(text(), "Аудитории")]')

class MainPageLocators(BasePageLocators):
    AUTH_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    
    LOGIN = (By.XPATH, '//*[@placeholder="Email или номер телефона" and @name="email"]')
    PASSWORD = (By.XPATH, '//*[@placeholder="Пароль" and @name="password"]')

    LOG_IN_BUTTON = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')

class CampaignsPageLocators(BasePageLocators):
    CREATE_NEW_CAMP_BUTTON = (By.CLASS_NAME, 'button-module-textWrapper-3LNyYP')

    CAMPAIGNS_TABLE = (By.XPATH, '//span[contains(text(), "Название")]')
                       
class CreateCampLocators(BasePageLocators):
    TRAFFIC_BUTTON = (By.XPATH, '//div[contains(text(), "Трафик")]')
    TEASER_FORMAT_BUTTON = (By.XPATH, '//span[contains(text(), "Тизер")]')

    TITLE_FIELD = (By.XPATH, '//li[@data-name="title"]//input')
    TEXT_FIELD = (By.XPATH, '//li[@data-class-name="TextArea"]//textarea')

    TEMPLATE_BANNER_IMAGE = (By.XPATH, '//div[@class="js-medialib"]//div[@draggable="true"]')
    UPLOAD_BANNER_IMAGE_BUTTON = (By.XPATH, '//div[@class="banner-preview__middle"]//div[@class="banner-preview__image js-image-wrap"]')

    URL_FIELD = (By.XPATH, '//*[@placeholder="Введите ссылку"]')

    CREATE_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать кампанию")]')

    CAMPAIGN_NAME = (By.XPATH, '//div[@class="campaign-name"]//input')

class SegmentsPageLocators(BasePageLocators):
    CREATE_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать сегмент")]')

    SEGMENTS_TABLE = (By.XPATH, '//span[contains(text(), "Имя сегмента")]')

    SEGMENT_ROW = (By.XPATH, '//a[contains(text(), "{}")]')

    DELETE_SEGMENT_CROSS = (By.XPATH, '//div[@data-test="remove-{} row-{}"]//span')

    CONFIRM_DELETE = (By.XPATH, '//div[@class="button__text" and contains(text(), "Удалить")]')

class CreateSegmentLocators(BasePageLocators):
    SEGMENT_CHECKBOX = (By.XPATH, '//input[@type="checkbox"]')

    ADD_SEGMENT_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Добавить сегмент")]')

    SEGMENT_NAME = (By.XPATH, '//div[@class="js-segment-name"]//input')

    CREATE_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать сегмент")]')