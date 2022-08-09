from selenium import webdriver
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome()
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

# maximizing the browser window
driver.maximize_window()

# sending a email to a login page
email_login_input = driver.find_element("id", "input-email")
email_login_input.clear()
email_login_input.send_keys("pab@yahoo.com")

# sending a password to a login page
password_login_input = driver.find_element("id", "input-password")
password_login_input.clear()
password_login_input.send_keys("password")

# sending a email to a login page
email_login_input = driver.find_element("id", "input-email")
email_login_input.clear()
email_login_input.send_keys("pab@yahoo.com")

# clicking a button to go to the registration page
new_registrant_btn = driver.find_element("xpath", "//a[contains(text(), 'Continue')]")
new_registrant_btn.click()

# filling fields/checking 'required' on the registration page
firstname_field = driver.find_element("xpath", "//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class
firstname_input = driver.find_element("id", "input-firstname")
firstname_input.clear()
firstname_input.send_keys("Evgeny")

lastname_field = driver.find_element("xpath", "//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class
lastname_input = driver.find_element("id", "input-lastname")
lastname_input.clear()
lastname_input.send_keys("Abdulin")

email_field = driver.find_element("xpath", "//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class
email_input = driver.find_element("id", "input-email")
email_input.clear()
email_input.send_keys("abdulin.evgeny@gmail.com")

telephone_field = driver.find_element("xpath", "//fieldset/div[4]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class
telephone_input = driver.find_element("id", "input-telephone")
telephone_input.clear()
telephone_input.send_keys("512-888-8888")

fax_input = driver.find_element("id", "input-fax")
fax_input.clear()
fax_input.send_keys("512-999-9999")

company_input = driver.find_element("id", "input-company")
company_input.clear()
company_input.send_keys("Texas State University")

address1_field = driver.find_element("xpath", "//fieldset[2]/div[2]")
address1_field_class = address1_field.get_attribute("class")
assert "required" in address1_field_class
address1_input = driver.find_element("id", "input-address-1")
address1_input.clear()
address1_input.send_keys("601 University Drive")

address2_input = driver.find_element("id", "input-address-2")
address2_input.clear()
address2_input.send_keys("Apt X")

city_field = driver.find_element("xpath", "//fieldset[2]/div[4]")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class
city_input = driver.find_element("id", "input-city")
city_input.clear()
city_input.send_keys("San Marcos")

postcode_input = driver.find_element("id", "input-postcode")
postcode_input.clear()
postcode_input.send_keys("78666-4684")

password_field = driver.find_element("xpath", "//fieldset[3]/div[1]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
password_input = driver.find_element("id", "input-password")
password_input.clear()
password_input.send_keys("superpassword")

confirm_field = driver.find_element("xpath", "//fieldset[3]/div[2]")
confirm_field_class = confirm_field.get_attribute("class")
assert "required" in confirm_field_class
confirm_input = driver.find_element("id", "input-confirm")
confirm_input.clear()
confirm_input.send_keys("superpassword")

continue_btn = driver.find_element("xpath", "//input[@value='Continue']")
