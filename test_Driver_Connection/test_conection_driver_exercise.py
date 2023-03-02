import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

global driver


class Test_WebDriver_Object_Methods:

    @pytest.fixture()
    def open_browser(self):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.imdb.com/")
        driver.maximize_window()

    def teardown_class(self):
        driver.quit()

    def test_1(self, open_browser):
        driver.refresh()
        web_title = "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"
        web_name = "https://www.imdb.com/"
        assert web_title == driver.title
        assert web_name == driver.current_url
        print("\nTitle is: " + web_title)
        print("URL is: " + web_name)

    def test_2(self, open_browser):
        driver.get("https://google.com")
        driver.get("https://bing.com")
        driver.back()
        print(driver.title)
        source = driver.page_source
        if "bubble" in source:
            print("Exist")
        else:
            print("Not Exist")

    def test_drivers(self):
        global driver

        # Open Chrome
        driver = webdriver.Chrome(ChromeDriverManager().install())
        time.sleep(2)
        driver.quit()

        # Open Edge
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        time.sleep(2)
        driver.quit()

        # Open Firefox
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        time.sleep(2)
        driver.quit()
        #
        # # Open Opera
        # driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        # time.sleep(2)
        # driver.quit()
