from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageElement:
    def __init__(self, driver: WebDriver, locator: Tuple[str, str]):
        self.driver = driver
        self.locator = locator

    def _get_el(self) -> WebElement:
        """Find element by its locator.

        TODO:
            1. Catch StaleElementReferenceException and re-try the search.
            2. Get different non-standard attributes.
            3. Write down typical expectations
        """
        return self.driver.find_element(*self.locator)

    def click(self) -> None:
        """Click on the element.

        TODO:
            1. Catch StaleElementReferenceException and re-try the search.
        """
        self._get_el().click()

    def send_keys(self, value: str) -> None:
        self._get_el().send_keys(value)
