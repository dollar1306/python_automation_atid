import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# for firefox browser
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

class Test_driver_Connection:
    @pytest.fixture()
    def open_browser(self):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # to open firefox browser
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://google.com")
        yield
        driver.quit()

    def test_1(self, open_browser):
        print("\nTitle is: " + driver.title)
        print("URL is: " + driver.current_url)
