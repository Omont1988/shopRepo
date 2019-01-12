from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


def find_element(driver, locator):
    delay = 5  # seconds
    try:
        return WebDriverWait(driver, delay).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        print("element {} was not found".format(locator))


def find_elements(driver, locator):
    delay = 5  # seconds
    try:
        return WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located(locator))

    except TimeoutException:
        print("elements {} was not found".format(locator))


def click(driver, locator):
    el = find_element(driver, locator)
    el.click()


def type_text(driver, locator, text):
    el = find_element(driver, locator)
    el.click()
    el.send_keys(text)


def get_text(driver, locator):
    el = find_element(driver, locator)
    return el.text
