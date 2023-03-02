from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLocatorsAdvanced:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_locators.html")

    def teardown_class(cls):
        driver.quit()

    def test_verify_locators(self):
        locator_by_id = driver.find_element(By.ID, "locator_id")
        print(locator_by_id)
        print(locator_by_id.text)

        locator_by_name = driver.find_element(By.NAME, "locator_name")
        print(locator_by_name)
        print(locator_by_name.text)

        locator_by_class_name = driver.find_element(By.CLASS_NAME, "locator_class")
        print(locator_by_class_name)
        print(locator_by_class_name.text)

        locator_by_tag = driver.find_element(By.CSS_SELECTOR, "#contact_info_left > div.locator_class")
        print(locator_by_tag)
        print(locator_by_tag.text)

        locator_by_link = driver.find_element(By.LINK_TEXT, "myLocator(5)")
        print(locator_by_link)
        print(locator_by_link.text)

        locator_by_partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Find my locator")
        print(locator_by_partial_link)
        print(locator_by_partial_link.text)

        locator_by_css = driver.find_element(By.CSS_SELECTOR, "input[value='Find my locator (7)']")
        print(locator_by_css)
        print(locator_by_css.text)

        locator_by_xpath = driver.find_element(By.XPATH, "//*[@id='contact_info_left']/button")
        print(locator_by_xpath)
        print(locator_by_xpath.text)
