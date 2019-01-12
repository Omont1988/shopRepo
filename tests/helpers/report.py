import allure
import moment
from allure.constants import AttachmentType

now = moment.now().strftime("%d-%m-%Y")

def save_screenshot(driver, name):
    # driver.get_screenshot_as_file(os.path.join(screen_path(), name + '-' + now + ".png"))
    allure.attach(name + "-" + now, driver.get_screenshot_as_png(), type=AttachmentType.PNG)
