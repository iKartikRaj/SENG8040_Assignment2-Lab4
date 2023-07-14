# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Conestoga College homepage
driver.get("https://www.conestogac.on.ca")
time.sleep(3)

# Clicking on the login button
login_button = driver.find_element("xpath", "/html/body/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div/button/span")
login_button.click()

# Waiting for the login page to load
time.sleep(5)

# Clicking on the student portal button
student_portal_button = driver.find_element("xpath", "/html/body/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/div[3]/div/div/a[2]")
student_portal_button.click()

# Waiting for the student portal page to load
time.sleep(5)

# Switching to the student portal window
driver.switch_to.window(driver.window_handles[-1])

# Closing the webdriver
driver.close()
