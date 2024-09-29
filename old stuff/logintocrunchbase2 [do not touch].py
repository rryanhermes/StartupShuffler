from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Set up Chrome options (not headless in this case)
chrome_options = Options()

# Use ChromeDriverManager to automatically get the correct ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Define the login URL
login_url = 'https://www.crunchbase.com/login'

# Open the login page
driver.get(login_url)

# Function to enter email slowly with retries if stale element occurs
def enter_email_slowly(driver, email):
    retries = 3
    for attempt in range(retries):
        try:
            email_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@name="email"]'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", email_input)
            sleep(1)

            for character in email:
                email_input.send_keys(character)
                sleep(0.1)
            print("Email entered successfully.")
            return
        except Exception as e:
            print(f"Attempt {attempt + 1} failed with error: {e}")
            if attempt == retries - 1:
                raise

try:
    enter_email_slowly(driver, "ryangrooverburner@yahoo.com")

    # Enter password
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]'))
    )
    password_input.send_keys("Ryanh22374!")
    print("Password entered successfully.")

    # Click login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )
    login_button.click()
    print("Login button clicked.")

    # After logging in, navigate to the WhatsApp company page while staying logged in
    company_url = "https://www.crunchbase.com/organization/whatsapp"
    driver.get(company_url)
    print("Navigated to WhatsApp company page.")

    # Wait for the "Verify email to view" button to appear and be clickable
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//a[@class="primary"]'))
    )
    
    # Wait 2 seconds to ensure everything is fully loaded
    sleep(2)

    # Relocate and click the "Verify email to view" button after the delay to avoid stale element reference
    verify_email_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="primary"]'))
    )
    verify_email_button.click()
    print("Verify email button clicked successfully.")

    # Wait to observe the results before closing
    sleep(60)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
