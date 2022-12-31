import time
import pytest
from selenium import webdriver
from AtideStore.BaseTest.locator import *

# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_shop_now():
    driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://atid.store/")

    shop_now = driver.find_element(By.XPATH, shop_now_xpath)
    shop_now.click()

    driver.find_element(By.XPATH, linkedProductName).click()
    time.sleep(1)

    adt_cart_button = driver.find_element(By.XPATH, add_cart_rel)
    adt_cart_button.click()
    view_product_on_cart = driver.find_element(By.XPATH, view_cart_rel)
    view_product_on_cart.click()

    coupon = driver.find_element(By.XPATH, coupon_code_rel)
    coupon.send_keys("come3")

    apply_cop = driver.find_element(By.XPATH, apply_coupon)
    apply_cop.click()
    time.sleep(8)
    price_a = driver.find_element(By.TAG_NAME, price).text
    assert price_a == "150.00 ₪"


def test_contactMe():
    driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, contact_us).click()
    time.sleep(2)
    driver.find_element(By.XPATH, con_us_customer_name_re).send_keys("zemene")
    time.sleep(1)
    driver.find_element(By.XPATH, contact_us_sub_rep).send_keys("qa")
    time.sleep(1)
    driver.find_element(By.XPATH, cont_us_email_rel).send_keys("zemeneabinet06@gmail.com")
    time.sleep(5)
    driver.find_element(By.XPATH, cont_message_box_rel).send_keys("This is first test in qa course ")
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, con_message_cssSe).click()
    time.sleep(12)


def test_about_us():
    driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, about_us_repath).click()
    driver.find_element(By.TAG_NAME, about_us_tag_name).click()
    time.sleep(12)

    driver.find_element(By.XPATH, about_us_tag_name_txt).click()
    time.sleep(10)


def test_accessories():
    driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, accessoriesRel).click()


def test_to_download_on_phone():
    driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, apple_store_rel).click()
    time.sleep(4)
    driver.find_element(By.XPATH, google_play_rel).click()
    time.sleep(5)


# def test_power_by_atide():
#     driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
#     driver = webdriver.Chrome(service=driver_service)
#     driver.get("https://atid.store/")
#     time.sleep(5)
#
# driver.find_element(By.LINK_TEXT, pw_by_atid_collage).click()
# time.sleep(5)

def test_store():
    driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://atid.store/")

    driver.find_element(By.XPATH, store_test).click()
    time.sleep(1)
    driver.find_element(By.XPATH, store_pro).click()

    time.sleep(1)
    driver.find_element(By.XPATH, stor_pro_add_but).click()
    time.sleep(1)
    driver.find_element(By.XPATH, added_pro_view).click()

    time.sleep(2)

    product_name = driver.find_element(By.XPATH, check_product_name).text

    assert product_name == 'ATID Black Shoes'


def test_men():
    driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, men_test).click()

    time.sleep(1)
    driver.find_element(By.XPATH, men_pro).click()
    time.sleep(1)
    driver.find_element(By.XPATH, add_men_pro).click()
    time.sleep(1)
    driver.find_element(By.XPATH, men_product_view).click()

    time.sleep(3)
    driver.find_element(By.XPATH, men_cart_check).click()
    time.sleep(3)

    productName = driver.find_element(By.XPATH, men_product_name).text
    assert productName == "ATID Green Tshirt"


def test_women():
    driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, women_test).click()

    time.sleep(1)
    driver.find_element(By.XPATH, women_pro_view).click()

    time.sleep(1)
    driver.find_element(By.XPATH, women_add_product).click()
    time.sleep(1)
    driver.find_element(By.XPATH, women_product_added_view).click()

    time.sleep(3)
    driver.find_element(By.NAME, women_coupon).send_keys("abebe12")
    time.sleep(4)

    driver.find_element(By.XPATH, women_product_apply_copon).click()
    time.sleep(2)
    prduct_name = driver.find_element(By.XPATH, women_produc_name).text
    assert 'Bright Red Bag' == prduct_name


def test_accessorries():
    driver_service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://atid.store/")

    driver.get("https://atid.store/")

    driver.find_element(By.XPATH, accessory_test).click()
    time.sleep(1)
    driver.find_element(By.XPATH, accessory_products).click()

    time.sleep(1)
    driver.find_element(By.XPATH, accessor_add_cart).click()
    time.sleep(1)
    driver.find_element(By.XPATH, view_added_accesory_pro).click()
    time.sleep(2)
    driver.find_element(By.NAME, coupon_accessory).send_keys("accessories")
    time.sleep(5)
    driver.find_element(By.XPATH, click_apply_coupon).click()
    time.sleep(2)
    productName = driver.find_element(By.XPATH, accessory_product_name).text
    assert productName == "Black Over-the-shoulder Handbag"
