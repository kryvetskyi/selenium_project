
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCreateGroup:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()
  
    def test_create_group(self):
        # Test name: test_create_group
        # Step # | name | target | value
        #  1 | open | /addressbook/index.php |
        self.driver.get("http://localhost:8888/addressbook/index.php")
        # 2 | setWindowSize | 1200x900 |
        self.driver.set_window_size(1200, 900)
        # 3 | type | name=user | admin
        self.driver.find_element(By.NAME, "user").send_keys("admin")
        # 4 | type | name=pass | secret
        self.driver.find_element(By.NAME, "pass").send_keys("secret")
        # 5 | click | css=input:nth-child(7) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
        # 6 | click | linkText=groups |
        self.driver.find_element(By.LINK_TEXT, "groups").click()
        # 7 | click | name=new |
        self.driver.find_element(By.NAME, "new").click()
        # 8 | click | name=group_name |
        self.driver.find_element(By.NAME, "group_name").click()
        # 9 | type | name=group_name | kjsahf
        self.driver.find_element(By.NAME, "group_name").send_keys("kjsahf")
        # 10 | click | name=group_header |
        self.driver.find_element(By.NAME, "group_header").click()
        # 11 | type | name=group_header | asf
        self.driver.find_element(By.NAME, "group_header").send_keys("asf")
        # 12 | click | name=group_footer |
        self.driver.find_element(By.NAME, "group_footer").click()
        # 13 | type | name=group_footer | asf
        self.driver.find_element(By.NAME, "group_footer").send_keys("asf")
        # 14 | click | name=submit |
        self.driver.find_element(By.NAME, "submit").click()
        # 15 | click | linkText=group page |
        self.driver.find_element(By.LINK_TEXT, "group page").click()
        # 16 | click | linkText=Logout |
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        #   17 | type | name=user | admin
        self.driver.find_element(By.NAME, "user").send_keys("admin")
        # 18 | type | name=pass | secret
        self.driver.find_element(By.NAME, "pass").send_keys("secret")
