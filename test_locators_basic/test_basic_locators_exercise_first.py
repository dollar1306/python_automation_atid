from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Locators_Basic_first:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.selenium.dev/")
        driver.maximize_window()

    def teardown_class(self):
        driver.quit()

    def test_verify_locator(self):
        print(driver.find_element(By.CLASS_NAME, "navbar-brand"))
        print(driver.find_element(By.CLASS_NAME, "navbar-logo"))
        print(driver.find_element(By.ID, "selenium_logo"))
        print(driver.find_element(By.TAG_NAME, "svg"))
        print(driver.find_elements(By.TAG_NAME, "svg")[0])

        links = driver.find_elements(By.TAG_NAME, "a")
        Selenium_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Selenium")
        selenium_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "selenium")
        print("Number of total links in page: " + str(len(links)))
        print("Number of links in page with word: Selenium is: " + str(len(Selenium_links)))
        print("Number of links in page with word: selenium is: " + str(len(selenium_links)))


