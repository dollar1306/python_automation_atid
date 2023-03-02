from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Locators_Basic_second:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.wikipedia.org/")
        driver.maximize_window()

    def teardown_class(self):
        driver.quit()

    def test_verify_locator(self):
        logo = driver.find_element(By.CLASS_NAME, "central-featured-logo")
        search_field = driver.find_element(By.ID, "search-form")
        select_language = driver.find_element(By.ID, "searchLanguage")
        footer_side = driver.find_element(By.CLASS_NAME, "footer-sidebar-text")
        wiki_elements = [logo, search_field, select_language, footer_side]
        print("\n")
        for element in reversed(wiki_elements):
            print(element)

