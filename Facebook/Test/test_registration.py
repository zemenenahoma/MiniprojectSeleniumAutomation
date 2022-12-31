import pytest
import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Facebook.BaseTast.locator import *

driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)


def test_valid_filling():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, Creat_feild).click()
    time.sleep(4)

    firstName = driver.find_element(By.NAME, first_name)
    firstName.clear()
    firstName.send_keys("habtam")

    time.sleep(5)
    driver.find_element(By.NAME, last_name).send_keys("nahom")
    time.sleep(3)
    driver.find_element(By.NAME, email).send_keys("zemeneabinet06@gmail.com")
    time.sleep(3)
    driver.find_element(By.NAME, password).send_keys("NM1890")
    driver.find_element(By.NAME, birthdate_moth).send_keys("04")
    driver.find_element(By.NAME, birthdate_day).send_keys("12")
    driver.find_element(By.NAME, birthdate_year).send_keys("1996")
    driver.find_element(By.NAME, male_gender).click()
    driver.find_element(By.NAME, signUp).click()
    time.sleep(5)


def test_invalid_email_filling():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, Creat_feild).click()
    time.sleep(4)

    firstName = driver.find_element(By.NAME, first_name)
    firstName.clear()
    firstName.send_keys("habtam")

    time.sleep(5)
    driver.find_element(By.NAME, last_name).send_keys("nahom")
    time.sleep(3)
    driver.find_element(By.NAME, email).send_keys("zemeneabinetgmail.com")
    time.sleep(3)
    driver.find_element(By.NAME, password).send_keys("NM1890")
    driver.find_element(By.NAME, birthdate_moth).send_keys("04")
    driver.find_element(By.NAME, birthdate_day).send_keys("12")
    driver.find_element(By.NAME, birthdate_year).send_keys("1996")
    driver.find_element(By.NAME, male_gender).click()
    driver.find_element(By.NAME, signUp).click()
    time.sleep(5)


def test_empty_firstName_filling():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, Creat_feild).click()
    time.sleep(4)

    firstName = driver.find_element(By.NAME, first_name)
    firstName.clear()
    firstName.send_keys(" ")

    time.sleep(5)
    driver.find_element(By.NAME, last_name).send_keys("nahom")
    time.sleep(3)
    driver.find_element(By.NAME, email).send_keys("zemeneabinet06@gmail.com")
    time.sleep(3)
    driver.find_element(By.NAME, password).send_keys("NM1890")
    driver.find_element(By.NAME, birthdate_moth).send_keys("04")
    driver.find_element(By.NAME, birthdate_day).send_keys("12")
    driver.find_element(By.NAME, birthdate_year).send_keys("1996")
    driver.find_element(By.NAME, male_gender).click()
    driver.find_element(By.NAME, signUp).click()
    time.sleep(5)


def test_changing_month_date_place_filling():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, Creat_feild).click()
    time.sleep(4)

    firstName = driver.find_element(By.NAME, first_name)
    firstName.clear()
    firstName.send_keys("habtam")

    time.sleep(5)
    driver.find_element(By.NAME, last_name).send_keys("nahom")
    time.sleep(3)
    driver.find_element(By.NAME, email).send_keys("zemeneabinet06@gmail.com")
    time.sleep(3)
    driver.find_element(By.NAME, password).send_keys("NM1890")
    driver.find_element(By.NAME, birthdate_moth).send_keys("04")
    driver.find_element(By.NAME, birthdate_day).send_keys("12")
    driver.find_element(By.NAME, birthdate_year).send_keys("1996")
    driver.find_element(By.NAME, male_gender).click()
    driver.find_element(By.NAME, signUp).click()
    time.sleep(5)


def test_without_clicking_gender_filling():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, Creat_feild).click()
    time.sleep(4)

    firstName = driver.find_element(By.NAME, first_name)
    firstName.clear()
    firstName.send_keys("habtam")

    time.sleep(5)
    driver.find_element(By.NAME, last_name).send_keys("nahom")
    time.sleep(3)
    driver.find_element(By.NAME, email).send_keys("zemeneabinet06@gmail.com")
    time.sleep(3)
    driver.find_element(By.NAME, password).send_keys("NM1890")
    driver.find_element(By.NAME, birthdate_moth).send_keys("04")
    driver.find_element(By.NAME, birthdate_day).send_keys("12")
    driver.find_element(By.NAME, birthdate_year).send_keys("1996")
    # driver.find_element(By.NAME, male_gender).click()
    driver.find_element(By.NAME, signUp).click()
    time.sleep(5)


def test_only_Number_password_filling():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, Creat_feild).click()
    time.sleep(4)

    firstName = driver.find_element(By.NAME, first_name)
    firstName.clear()
    firstName.send_keys("habtam")

    time.sleep(5)
    driver.find_element(By.NAME, last_name).send_keys("nahom")
    time.sleep(3)
    driver.find_element(By.NAME, email).send_keys("zemeneabinet06@gmail.com")
    time.sleep(3)
    driver.find_element(By.NAME, password).send_keys("451890")
    driver.find_element(By.NAME, birthdate_moth).send_keys("04")
    driver.find_element(By.NAME, birthdate_day).send_keys("12")
    driver.find_element(By.NAME, birthdate_year).send_keys("1996")
    driver.find_element(By.NAME, male_gender).click()
    driver.find_element(By.NAME, signUp).click()
    time.sleep(5)


def test_numbers_inNaming_fields_filling():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, Creat_feild).click()
    time.sleep(4)

    firstName = driver.find_element(By.NAME, first_name)
    firstName.clear()
    firstName.send_keys("14252")

    time.sleep(5)
    driver.find_element(By.NAME, last_name).send_keys("854620")
    time.sleep(3)
    driver.find_element(By.NAME, email).send_keys("zemeneabinet06@gmail.com")
    time.sleep(3)
    driver.find_element(By.NAME, password).send_keys("NM1890")
    driver.find_element(By.NAME, birthdate_moth).send_keys("04")
    driver.find_element(By.NAME, birthdate_day).send_keys("12")
    driver.find_element(By.NAME, birthdate_year).send_keys("1996")
    driver.find_element(By.NAME, male_gender).click()
    driver.find_element(By.NAME, signUp).click()
    time.sleep(5)


def test_forgot_password():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, forgotPassword).click()
    time.sleep(5)
    driver.find_element(By.NAME, forgot_pass_name).send_keys("zemeneabinet06@gmail.com")
    time.sleep(7)
    driver.find_element(By.ID, search_forgot_password).click()
    time.sleep(30)


def test_forgot_password_wrong_email():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, forgotPassword).click()
    time.sleep(5)
    driver.find_element(By.NAME, forgot_pass_name).send_keys("zemeneabinet0mail.com")
    time.sleep(7)
    driver.find_element(By.ID, search_forgot_password).click()
    time.sleep(30)


def test_forgot_paswor_onlynumber():
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH, forgotPassword).click()
    time.sleep(5)
    driver.find_element(By.NAME, forgot_pass_name).send_keys("zemeneabinet06@gmail.com")
    time.sleep(7)
    driver.find_element(By.ID, search_forgot_password).click()
    time.sleep(30)
