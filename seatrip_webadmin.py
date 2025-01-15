# Author: Esmeralda Wangsa

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Function to save log to HTML file
def save_to_html(message):
    print(message)  # Print log to terminal
    with open("log_sea_trip_webadmin.html", "a", encoding="utf-8") as log_file:
        log_file.write(f"<p>{message}</p>\n")

# Setup driver and FirefoxOptions
service = Service("C:\\Users\\esmeralda.wangsa\\selenium-logisticsweb\\geckodriver.exe")
options = webdriver.FirefoxOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# Connect Selenium to Firefox browser
driver = webdriver.Firefox(service=service, options=options)

# Open the login page
driver.get("https://samplelogisticsweb.co.id/#/login")
save_to_html("Page Title: " + driver.title)

# Find email input field
try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/form/div/div[2]/div[1]/input"))
    )
    email_input.send_keys("esmeralda_adminlogistics@gmail.com")
    save_to_html("Email input field found.")
except Exception as e:
    save_to_html(f"Email input field not found! Error: {e}")

# Find password input field
try:
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/form/div/div[2]/div[2]/input"))
    )
    password_input.send_keys("123456")
    save_to_html("Password input field found.")
except Exception as e:
    save_to_html(f"Password input field not found! Error: {e}")

# Find login button
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()
    save_to_html("Login button found.")
except Exception as e:
    save_to_html(f"Login button not found! Error: {e}")

# Wait for a few seconds
time.sleep(3)

# Click the Web Admin button after login
try:
    additional_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/button[2]"))
    )
    additional_button.click()
    save_to_html("Web Admin button found.")
except Exception as e:
    save_to_html(f"Web Admin button not found! Error: {e}")

# Find "Sea Shipment" menu
try:
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/header/div[2]/div/div/div/input"))
    )
    search_input.click()  # Ensure the element is active
    search_input.send_keys("Sea Shipment")  # Enter text
    save_to_html("'Sea Shipment' text successfully typed.")

    time.sleep(2)  # Wait for a moment
    search_input.send_keys(Keys.RETURN)  # Press Enter key
    save_to_html("Sea Shipment page successfully opened.")
except Exception as e:
    save_to_html(f"Failed to open Sea Shipment page. Error: {e}")

# Create Sea Shipment
try:
    triplaut_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div/div/header/div/button[2]"))
    )
    triplaut_button.click()
    save_to_html("Listing Order for Sea Shipment creation successfully opened.")
except Exception as e:
    save_to_html(f"Failed to open listing order for Sea Shipment creation. Error: {e}")

# Wait for 7 seconds before entering data
time.sleep(7)

# Input Order ID
try:
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/div[1]/div[1]/input"))
    )
    input_field.click()  # Focus on input field
    input_field.send_keys("ALD2406190016")
    save_to_html("Order ID successfully entered.")
except Exception as e:
    save_to_html(f"Failed to input Order ID! Error: {e}")

# Wait for 5 seconds before proceeding
time.sleep(5)

# Process trip creation after inputting Order ID
try:
    # Click the checkbox on the first element
    checkbox_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/div[2]/div/div[1]/div[1]/span"))
    )
    checkbox_element.click()
    save_to_html("Checkbox successfully clicked.")

    # Click 'Continue Order' button
    select_order_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div[4]/button"))
    )
    select_order_button.click()
    save_to_html("'Continue Order' button successfully clicked.")
    time.sleep(5)  # Wait for 5 seconds

    # Click 'Continue' button
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div[4]/button[2]"))
    )
    confirm_button.click()
    save_to_html("'Continue' button successfully clicked.")
    time.sleep(20)  # Wait for 20 seconds

    # Click 'Select First Transporter' button
    select_transporter_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/div[2]/div[3]/div/div[2]/button"))
    )
    select_transporter_button.click()
    save_to_html("'Select First Transporter' button successfully clicked.")

    # Click 'Create Trip' button after selecting the first transporter
    create_trip_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div[4]/button[2]"))
    )
    create_trip_button.click()
    save_to_html("'Create Trip' button successfully clicked.")

    # Click 'Yes' after selecting the transporter
    yes_button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[3]/div/div/div[3]/button[2]"))
    )
    yes_button.click()
    save_to_html("'Yes' button successfully clicked.")
    time.sleep(3)  # Wait for 3 seconds

    alokasitpt_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div[2]"))
    )
    alokasitpt_input.click()  # Click dropdown element
    actions = ActionChains(driver)
    actions.send_keys("Operational Necessity").send_keys(Keys.RETURN).perform()
    save_to_html("Category of Reason successfully selected.")

    # Click 'Create Shipment' after selecting the reason
    createshipment_button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[3]/div/div[3]/button[2]"))
    )
    createshipment_button.click()
    save_to_html("'Create Shipment' button successfully clicked.")

    # Click 'Yes' button after creating the trip
    yes2_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[3]/div/div/div[3]/button[2]"))
    )
    yes2_button.click()
    save_to_html("Sea Shipment successfully created.")
except Exception as e:
    save_to_html(f"Failed to complete the trip creation process. Error: {e}")


# End the Selenium session
save_to_html("Sea Shipment script finished running.")
input("Press Enter to continue or close the script and browser...")

# driver.quit()  # Uncomment to close browser after script finishes