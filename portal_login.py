'''
With the correct email, pass, and OTP secret values, this script
can be used to automate the Partner Portal login

Author: Steve Reilly
'''

from selenium import webdriver
import pyotp

# Launch Firefox and navigate to the Partner Portal
browser = webdriver.Firefox()
browser.get("http://portal.dattobackup.com")

# Get login elements
username    = browser.find_element_by_id("form_username")
password    = browser.find_element_by_id("form_password")
submit_user = browser.find_element_by_id("form_submit")

# Log in to Portal
username.send_keys("EMAIL")
password.send_keys("PASSWORD")
submit_user.click()

# Get 2FA elements
otp        = browser.find_element_by_id("authy_token")
sumbit_otp = browser.find_element_by_name("submitButton")

# Set TOTP code
totp = pyotp.TOTP("OTP-SECRET")
code = totp.now()

# Submit 2FA OTP
otp.send_keys(code)
sumbit_otp.click()
