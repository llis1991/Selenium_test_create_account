import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_create_account_faild():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(1800, 1200)
    wait = WebDriverWait(driver, 10)
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys("xyz@gmail.com")
    driver.find_element(By.ID, "reg_password").send_keys("Selenium123456789!")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    assert driver. find_element(By.CLASS_NAME, "woocommerce-error").text == "Error: An account is already registered with your email address. Please log in."


def test_create_account_passed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(1800, 1200)
    wait = WebDriverWait(driver, 10)
    email = str(random.randint(0, 1000)) + "xyz@gmail.com"
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("Selenium123456789!")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()



