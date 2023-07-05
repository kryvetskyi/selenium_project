from selenium import webdriver
from selenium.common import WebDriverException

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, base_url, browser):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError("No such browser. Choose from ['chrome', 'firefox', 'edge']")
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        self.driver.get(self.base_url)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except WebDriverException:
            return False

    def destroy(self):
        self.driver.quit()
