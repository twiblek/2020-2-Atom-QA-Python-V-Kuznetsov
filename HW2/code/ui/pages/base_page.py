from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from ui.locators import basic_locators

RETRY_COUNT = 3


class BasePage(object):
    locators = basic_locators.BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None) -> WebElement:
        # нотация WebElement удобна тем, что у метода find становятся доступны методы WebElement
        # а это очень удобно

        return self.wait(timeout).until(EC.presence_of_element_located(locator))  # поиск элемента с ожиданием

    def click(self, locator, timeout=None):
        # попытки чтобы кликнуть
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def drag_and_drop(self, item, target):
        item_drag = self.find(item)
        target_drop = self.find(target)
        ActionChains(self.driver).drag_and_drop(item_drag, target_drop).perform() # Почему это не работает? Не могу придумать другой способ поместить баннер

    def count_elements(self, locator, count, timeout=1):
        # этот метод считает количество элементов на странице
        # until принимает функцию, а значит мы можем написать и использовать свою, в нашем случае это lambda функция
        # в этом методе мы ожидаем пока не появится нужное нам количество элементов на странице

        self.wait(timeout).until(lambda browser: len(browser.find_elements(*locator)) == count)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)