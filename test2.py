from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class TestSelenium(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('https://tutorialsninja.com/demo')
        self.search_field = self.driver.find_element(By.NAME, 'search')

    def tearDown(self):
        self.driver.quit()

    def test_add_to_shopping_cart(self):
        self.search_field.send_keys('iphone')
        self.search_field.send_keys(Keys.ENTER)

        cart_button = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
        cart_button.click()

        check_cart = self.driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')
        check_cart.click()

        self.assertTrue('product 11' in self.driver.page_source)

    def test_delete_from_shopping_cart(self):
        self.search_field.send_keys('iphone')
        self.search_field.send_keys(Keys.ENTER)

        cart_button = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
        cart_button.click()

        check_cart = self.driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')
        check_cart.click()

        self.assertTrue('product 11' in self.driver.page_source)

        remove_field = self.driver.find_element(By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]')
        remove_field.click()