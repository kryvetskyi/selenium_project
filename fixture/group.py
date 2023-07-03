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

        self.fill_group_form(group)

        # submit group creation
        driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def change_field_value(self, field_name, field_value):
        driver = self.app.driver
        if field_value is not None:
            driver.find_element(By.NAME, field_name).click()
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(field_value)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def modify_first_group(self, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()

        # open modification form
        driver.find_element(By.NAME, "edit").click()

        # fill the form
        self.fill_group_form(new_group_data)

        # submit
        driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()

        # select first group and click delete
        self.select_first_group()
        driver.find_element(By.NAME, "delete").click()

        self.return_to_groups_page()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

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
