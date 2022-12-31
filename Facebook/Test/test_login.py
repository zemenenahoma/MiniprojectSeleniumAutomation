from selenium import webdriver
import time
import pytest

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Facebook.BaseTast.locator import *

driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)


def test_fb_validly():
    driver.get("https://www.facebook.com/")

    valid_user_name = driver.find_element(By.XPATH, login_validly)
    valid_user_name.clear()
    valid_user_name.send_keys("+972534723118")
    time.sleep(2)
    valid_pass = driver.find_element(By.XPATH, password_validly)
    valid_pass.clear()
    valid_pass.send_keys("nm182551")
    time.sleep(1)

    click_button = driver.find_element(By.XPATH, login_button)
    click_button.click()
    time.sleep(1)


def test_invalid_Uname():
    driver.get("https://www.facebook.com/")

    valid_user_name = driver.find_element(By.XPATH, login_validly)
    valid_user_name.clear()
    valid_user_name.send_keys("2534723118")
    time.sleep(2)
    valid_pass = driver.find_element(By.XPATH, password_validly)
    valid_pass.clear()
    valid_pass.send_keys("nm182551")
    time.sleep(1)

    click_button = driver.find_element(By.XPATH, login_button)
    click_button.click()
    time.sleep(1)


def test_invalid_password():
    driver.get("https://www.facebook.com/")

    valid_user_name = driver.find_element(By.XPATH, login_validly)
    valid_user_name.clear()
    valid_user_name.send_keys("+972534723118")
    time.sleep(1)
    valid_pass = driver.find_element(By.XPATH, password_validly)
    valid_pass.clear()
    valid_pass.send_keys("nm182513")
    time.sleep(7)

    click_button = driver.find_element(By.XPATH, login_button)
    click_button.click()
    time.sleep(1)


def test_empty_uname():
    driver.get("https://www.facebook.com/")

    valid_user_name = driver.find_element(By.XPATH, login_validly)
    valid_user_name.clear()
    valid_user_name.send_keys(" ")
    time.sleep(1)
    valid_pass = driver.find_element(By.XPATH, password_validly)
    valid_pass.clear()
    valid_pass.send_keys("nm182513")
    time.sleep(1)

    click_button = driver.find_element(By.XPATH, login_button)
    click_button.click()
    time.sleep(2)


def test_empty_password():
    driver.get("https://www.facebook.com/")

    valid_user_name = driver.find_element(By.XPATH, login_validly)
    valid_user_name.clear()
    valid_user_name.send_keys("+972534723118")
    time.sleep(1)
    valid_pass = driver.find_element(By.XPATH, password_validly)
    valid_pass.clear()
    valid_pass.send_keys(" ")
    time.sleep(1)

    click_button = driver.find_element(By.XPATH, login_button)
    click_button.click()
    time.sleep(2)
    # h = driver.find_element(By.XPATH,first_name)
