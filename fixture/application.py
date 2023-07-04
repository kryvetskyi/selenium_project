from selenium import webdriver
from selenium.common import WebDriverException

from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost:8888/addressbook/")

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except WebDriverException:
            return False

    def destroy(self):
        self.driver.quit()
