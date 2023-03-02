import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Test_WebDriver_Object_Methods:
    @pytest.fixture()
    def open_browser(self):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://google.com")
        yield
        driver.quit()

    def test_1(self, open_browser):
        print("\nTitle is: " + driver.title)
        print("URL is: " + driver.current_url)
