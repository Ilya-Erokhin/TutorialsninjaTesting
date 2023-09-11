""" Page object model for Search Page"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class SearchPage:
    """Page object model for Search Page."""

    def __init__(self, driver: WebDriver):
        """Default constructor.

        :param driver: WebDriver instance.
        """
        self.driver = driver

    def open(self) -> None:
        """Navigate browser to the search page."""
        self.driver.get(
            "https://tutorialsninja.com/demo/index.php?route=product/search"
        )

    def set_search_query(self, query: str) -> None:
        """Input keyword (In the Site Header).

        :param query: search query.
        """
        self.driver.find_element(By.NAME, "search").send_keys(query)

    def click_search(self) -> None:
        """Click search in the header."""
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()

    def set_search_criteria(self, query: str) -> None:
        """Input keyword in Search Criteria section.

        :param query: Search query.
        """
        self.driver.find_element(
            By.XPATH, "//input[@placeholder='Keywords']"
        ).send_keys(query)

    def click_search_criteria_button(self) -> None:
        """Click on search button, below Search Criteria."""
        self.driver.find_element(By.ID, "button-search").click()
