from selenium.webdriver.common.by import By

## Login fields
name_field = (By.XPATH, "//table[@class='credentials'][1]//input[@type='text']")
passw_field = (By.XPATH, "//table[@class='credentials'][1]//input[@type='password']")
login_button = (By.XPATH, "//button[.='Login']")
user_footer = (By.XPATH, "//div[@class = 'footer ng-binding']")
login_link = (By.PARTIAL_LINK_TEXT, "Login")
error_credentials_message = (By.XPATH, '//div[@class="message ng-binding"]')
