from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the web application
driver.get("https://example.com/login")

# Locate the username and password fields
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Enter username and password
username_field.send_keys("Ayesha")
password_field.send_keys("Ayesha123")

# Locate and click the login button
login_button = driver.find_element(By.ID, "loginButton")
login_button.click()

# Wait for the login process to complete
time.sleep(5)

# Verify login by checking if the logout button is displayed
try:
    logout_button = driver.find_element(By.ID, "logoutButton")
    assert logout_button.is_displayed()
    print("Login test passed.")
    
    # Click the logout button to log out
    logout_button.click()
    
    # Wait for the logout process to complete
    time.sleep(5)
    
    # Verify logout by checking if the login button is displayed again
    login_button = driver.find_element(By.ID, "loginButton")
    assert login_button.is_displayed()
    print("Logout test passed.")
except Exception as e:
    print("Login/Logout test failed.", e)

# Close the browser
driver.quit()
