from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from home_page import HomePage
from search_page import SearchPage


def test():
    driver = webdriver.Chrome(
        service=ChromiumService(
            ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()
        )
    )

    home_page = HomePage(driver)
    home_page.open()
    home_page.set_search_query("apple")
    home_page.open()

    assert "MacBook" in driver.page_source

    driver.quit()


def test_search_home():
    driver = webdriver.Chrome(
        service=ChromiumService(
            ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()
        )
    )

    home_page = HomePage(driver)
    home_page.open()
    home_page.set_search_query("Samsung")
    home_page.click_search()

    assert "Search - Samsung" in driver.page_source

    driver.quit()


def test_search_page():
    driver = webdriver.Chrome(
        service=ChromiumService(
            ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()
        )
    )

    search_page = SearchPage(driver)
    search_page.open()
    search_page.set_search_criteria("Samsung")
    search_page.click_search_criteria_button()

    assert "Samsung SyncMaster 941BW" in driver.page_source

    driver.quit()
