class BasePage(object):
    base_url = 'http://web:8080'

    def __init__(self, webdriver, route=None):
        self.webdriver = webdriver
        if route is not None:
            self.route = self.base_url + route
        else:
            self.route = self.base_url

    def open_page(self):
        self.webdriver.get(self.route)
