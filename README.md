# Web Logistics Automation Testing using Selenium

## Description

This project automates testing for **Web Logistics** using **Selenium** and **Python**. The automation includes:

1. **Login Automation**: Automates logging into the Web Admin page.
2. **Ground Shipping Order Creation**: Automates the creation of a Ground Shipping order.
3. **Sea Shipment Creation**: Automates the creation of a Sea Shipment order.

All actions are logged in HTML files for easy review.

## Project Structure

- `login_webadmin.py`: Automates the login process on the Web Admin page using **Chrome**.
- `groundtrip_webadmin.py`: Automates the creation of a Ground Shipping order using **Firefox**.
- `seatrip_webadmin.py`: Automates the creation of a Sea Shipment order using **Firefox**.
- `log_ground_trip_webadmin.html`: Contains logs for the Ground Shipping automation process.
- `log_sea_trip_webadmin.html`: Contains logs for the Sea Shipment automation process.
- `chromedriver.exe`: WebDriver for Chrome to run the `login_webadmin.py` script.
- `geckodriver.exe`: WebDriver for Firefox to run the `groundtrip_webadmin.py` and `seatrip_webadmin.py` script.

## Installation

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/esmeraldawgs/selenium-logisticsweb.git
   cd repository

2. **Install Dependencies**
   Install the necessary Python dependencies:
   `pip install selenium`

3. **Download WebDrivers**
   Download and place the following drivers in the repository folder:
   Chrome: ChromeDriver
   Firefox: GeckoDriver
   Ensure the drivers are named as chromedriver.exe and geckodriver.exe and placed in the project folder.
   
5. **Running Tests**
   To execute the automation scripts:
   `python login_webadmin.py`
   `python groundtrip_webadmin.py`
   `python seatrip_webadmin.py`
