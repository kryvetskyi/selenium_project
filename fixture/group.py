from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()

        # init group creation
        driver.find_element(By.NAME, "new").click()

        # fill group form
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)

        # submit group creation
        driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()

        # select first group and click delete
        driver.find_element(By.NAME, "selected[]").click()
        driver.find_element(By.NAME, "delete").click()

        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "group page").click()

    def delete_group_by_index(self, index):
        driver = self.app.driver
        self.open_groups_page()

        # select group by index and  click delete
        try:
            driver.find_element(By.XPATH, f"//span[@class='group'][{index}]/input[@type='checkbox']").click()
        except NoSuchElementException:
            error_message = f"Can't find group by index {index}"
            raise AssertionError(error_message)

        driver.find_element(By.NAME, "delete").click()

        self.return_to_groups_page()
