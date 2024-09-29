from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import time

# Set up Chrome options
chrome_options = Options()

# Use ChromeDriverManager to automatically get the correct ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Define the login URL
login_url = 'https://mail.yahoo.com/n/inbox/priority?.src=ym&reason=myc'

# Open the login page
driver.get(login_url)

try:
    # Enter email
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )
    email_input.send_keys("ryangrooverburner@yahoo.com")  # Replace with your actual Yahoo email
    print("Email entered successfully.")
    
    # Click the Next button
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'login-signin'))
    )
    next_button.click()
    print("Next button clicked.")

    # Wait for the password field to appear and enter the password
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'password'))
    )
    password_input.send_keys("Ryanh22374!")  # Replace with your actual password
    print("Password entered successfully.")

    # Click the Sign in button
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )
    sign_in_button.click()
    print("Sign in button clicked.")

    time.sleep(5)

    # After logging in, navigate to the homepage
    inbox_url = "https://mail.yahoo.com/n/inbox/priority?.src=ym&reason=myc"
    WebDriverWait(driver, 10).until(
        EC.url_changes(login_url)  # Wait until the URL changes after login
    )
    driver.get(inbox_url)
    print("Navigated to Yahoo Mail homepage.")

    # Wait for 2 seconds after logging in
    time.sleep(2)

    # Click the "Check your mail" button
    inbox_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ybarMailLink'))
    )
    inbox_button.click()
    print("Inbox button clicked.")

    sleep(5)

    verification_code = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'P_ZWpIK5')))

    print(verification_code)
    # Wait to observe the results before closing
    sleep(600)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
