from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Locators_Basic:

    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://www.wikipedia.org/")
        driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_locators1(self):
        driver.find_element(By.ID, "searchInput")
        driver.find_element(By.CLASS_NAME, "pure-button-primary-progressive")
        driver.find_element(By.ID, "searchLanguage")
        driver.find_element(By.CLASS_NAME, "central-featured-logo")
        driver.get_screenshot_as_file(
            "C:/Users/AlexKuzmin/PycharmProjects/python_automation_atid/screen_shots/logoWiki.jpg")

