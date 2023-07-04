from selenium.webdriver.common.by import By

from models.group import Group


class GroupHelper:
    group_cache = None

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        if not (self.app.driver.current_url.endswith("/group.php") and
                len(self.app.driver.find_elements(By.NAME, "new")) > 0):
            self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        self.open_groups_page()

        # init group creation
        self.app.driver.find_element(By.NAME, "new").click()

        self.fill_group_form(group)

        # submit group creation
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def change_field_value(self, field_name, field_value):
        if field_value is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).clear()
            self.app.driver.find_element(By.NAME, field_name).send_keys(field_value)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def modify_first_group(self, new_group_data):
        self.open_groups_page()
        self.select_first_group()

        # open modification form
        self.app.driver.find_element(By.NAME, "edit").click()

        # fill the form
        self.fill_group_form(new_group_data)

        # submit
        self.app.driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.open_groups_page()

        # select first group and click delete
        self.select_first_group()
        self.app.driver.find_element(By.NAME, "delete").click()

        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        self.app.driver.find_element(By.NAME, "selected[]").click()

    def return_to_groups_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        self.open_groups_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))

    def get_all_groups(self):
        if self.group_cache is None:
            self.group_cache = []
            self.open_groups_page()
            all_groups_elements = self.app.driver.find_elements(By.XPATH, "//span[@class='group']")
            for el in all_groups_elements:
                text = el.text
                group_id = el.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=group_id))

        return list(self.group_cache)
