# Author: Esmeralda Wangsa

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Function to save logs to an HTML file
def save_to_html(message):
    print(message)  # Print log to the terminal
    with open("log_ground_trip_webadmin.html", "a", encoding="utf-8") as log_file:
        log_file.write(f"<p>{message}</p>\n")

# Setup Firefox driver and options
service = Service("C:\\Users\\esmeralda.wangsa\\selenium-logisticsweb\\geckodriver.exe")
options = webdriver.FirefoxOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# Start Firefox driver
driver = webdriver.Firefox(service=service, options=options)

# Open the login page
driver.get("https://samplelogisticsweb.co.id/#/login")
save_to_html("Page Title: " + driver.title)

# Locate and fill in the email input field
try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/form/div/div[2]/div[1]/input"))
    )
    email_input.send_keys("esmeralda_adminlogistics@gmail.com")
    save_to_html("Email input field located and email entered.")
except Exception as e:
    save_to_html(f"Email input field not found! Error: {e}")

# Locate and fill in the password input field
try:
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/form/div/div[2]/div[2]/input"))
    )
    password_input.send_keys("123456")
    save_to_html("Password input field located and password entered.")
except Exception as e:
    save_to_html(f"Password input field not found! Error: {e}")

# Locate and click the login button
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()
    save_to_html("Login button located and clicked.")
except Exception as e:
    save_to_html(f"Login button not found! Error: {e}")

# Wait for login to process
time.sleep(3)

# Click the Web Admin button after login
try:
    additional_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/button[2]"))
    )
    additional_button.click()
    save_to_html("Web Admin button located and clicked.")
except Exception as e:
    save_to_html(f"Web Admin button not found! Error: {e}")

# Locate and search for "Ground Shipping"
try:
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/header/div[2]/div/div/div/input"))
    )
    search_input.click()  # Focus the input field
    search_input.send_keys("Ground Shipping")  # Type the search term
    save_to_html("Text 'Ground Shipping' typed into search field.")

    time.sleep(2)  # Wait briefly
    search_input.send_keys(Keys.RETURN)  # Press Enter key to submit search
    save_to_html("Ground Shipping page successfully opened.")
except Exception as e:
    save_to_html(f"Failed to open Ground Shipping page. Error: {e}")

# Create a Ground Shipping order
try:
    ground_trip_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div/div/header/div/button[2]"))
    )
    ground_trip_button.click()
    save_to_html("Listing Order for creating Ground Shipping opened.")
except Exception as e:
    save_to_html(f"Failed to open listing order for Ground Shipping. Error: {e}")

# Wait before inputting data
time.sleep(10)

# Input the order ID
try:
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/div[1]/div[1]/input"))
    )
    input_field.click()  # Focus on the input field
    input_field.send_keys("ALD2501130001")
    save_to_html("Order ID successfully entered.")
except Exception as e:
    save_to_html(f"Order ID input failed! Error: {e}")

# Wait before proceeding
time.sleep(5)

# Process trip creation after order ID input
try:
    # Click the checkbox to select the first item
    checkbox_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/div[2]/div/div[1]/div[1]/span"))
    )
    checkbox_element.click()
    save_to_html("Checkbox selected.")

    # Click the 'Proceed Order' button
    select_order_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div[4]/button"))
    )
    select_order_button.click()
    save_to_html("'Proceed Order' button clicked.")
    time.sleep(5)  # Wait briefly

    # Click the 'Continue' button
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div[4]/button[2]"))
    )
    confirm_button.click()
    save_to_html("'Continue' button clicked.")
    time.sleep(20)  # Wait 20 seconds for processing

    # Click the 'Select First Transporter' button
    select_transporter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div/div/div[2]/button"))
    )
    select_transporter_button.click()
    save_to_html("'Select First Transporter' button clicked.")

    # Click the 'Create Trip' button
    create_trip_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div[4]/button[2]"))
    )
    create_trip_button.click()
    save_to_html("'Create Trip' button clicked.")

    # Click the 'Confirm' button after creating the trip
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[3]/div/div/div[3]/button[2]"))
    )
    confirm_button.click()
    save_to_html("Ground Shipping successfully created.")
except Exception as e:
    save_to_html(f"Failed to complete the trip creation process. Error: {e}")

# End the Selenium session and log completion
save_to_html("Ground Shipping script execution completed.")
input("Press Enter to continue or terminate the script and close the browser...")

# driver.quit()  # Uncomment if you want to close the browser after finishing