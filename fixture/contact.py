from selenium.webdriver.common.by import By

from models.contact import Contact


class ContactHelper:
    contact_cache = None

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, field_value):
        if field_value is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).clear()
            self.app.driver.find_element(By.NAME, field_name).send_keys(field_value)

    def get_contact_list(self):
        if self.contact_cache is None:
            self.contact_cache = []
            self.app.open_home_page()

            for row in self.app.driver.find_elements(By.XPATH, "//tr[@name='entry']"):
                cells = row.find_elements(By.TAG_NAME, "td")
                last_name = cells[1].text
                first_name = cells[2].text
                id_ = cells[0].find_element(By.TAG_NAME, "input").get_attribute('value')
                phones = cells[5].text

                self.contact_cache.append(Contact(id=id_,
                                                  first_name=first_name,
                                                  last_name=last_name,
                                                  phones_from_home_page=phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        self.app.open_home_page()
        row = self.app.driver.find_element(By.XPATH, f"//tr[@name='entry'][{index}]")
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_by_index(self, index):
        self.app.open_home_page()
        row = self.app.driver.find_element(By.XPATH, f"//tr[@name='entry'][{index}]")
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_view_page(self, index):
        self.open_contact_view_by_index(index)
        contact_data = self.app.driver.find_element(By.CSS_SELECTOR, "div#content").text.split('\n')
        contact_data = [i for i in contact_data if i != '']
        contact_id = self.app.driver.find_element(By.NAME, "id").get_attribute("value")
        first_name, last_name = contact_data[0].split(' ')
        home_phone = contact_data[1][3:]
        mobile_phone = contact_data[2][3:]
        work_phone = contact_data[3][3:]

        return Contact(id=contact_id,
                       first_name=first_name,
                       last_name=last_name,
                       home_phone=home_phone,
                       mobile_phone=mobile_phone,
                       work_phone=work_phone)

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        contact_id = self.app.driver.find_element(By.NAME, "id").get_attribute("value")
        first_name = self.app.driver.find_element(By.XPATH, "//input[@name='firstname']").get_attribute("value")
        last_name = self.app.driver.find_element(By.XPATH, "//input[@name='lastname']").get_attribute("value")
        home_phone = self.app.driver.find_element(By.XPATH, "//input[@name='home']").get_attribute("value")
        mobile_phone = self.app.driver.find_element(By.XPATH, "//input[@name='mobile']").get_attribute("value")
        work_phone = self.app.driver.find_element(By.XPATH, "//input[@name='work']").get_attribute("value")

        return Contact(id=contact_id,
                       first_name=first_name,
                       last_name=last_name,
                       home_phone=home_phone,
                       mobile_phone=mobile_phone,
                       work_phone=work_phone)
