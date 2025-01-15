# Author: Esmeralda Wangsa

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the login page
driver.get("https://samplelogisticsweb.co.id/#/login")

# Debug to view the page title
print("Page Title:", driver.title)

# Locate the email input field
try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/form/div/div[2]/div[1]/input"))
    )
    print("Email input field located.")
    email_input.send_keys("esmeralda_adminlogistics@gmail.com")
except Exception as e:
    print("Email input field not found!")
    print("Error:", str(e))

# Locate the password input field
try:
    password_input = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/form/div/div[2]/div[2]/input")
    print("Password input field located.")
    password_input.send_keys("123456")  # Replace "123456" with the actual password
except Exception as e:
    print(f"Password input field not found! Error: {e}")

# Locate the login button
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
    )
    print("Login button located.")
    login_button.click()
except Exception as e:
    print("Login button not found!")
    print("Error:", str(e))

# Click the Web Admin button after login
try:
    additional_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/button[2]"))
    )
    print("Web Admin button located.")
    additional_button.click()
except Exception as e:
    print(f"Web Admin button not found! Error: {e}")

# End the Selenium session
input("Press Enter to terminate the script and close the browser...")
driver.quit()