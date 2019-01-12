from selenium import webdriver
from selenium.webdriver.chrome.options import DesiredCapabilities as DS


class Session:
    def __init__(self):
        self.wd = webdriver.Remote(command_executor='http://hub:4444/wd/hub', desired_capabilities=DS.CHROME)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def close_session(self):
        return self.wd.quit
