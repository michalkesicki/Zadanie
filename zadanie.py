from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from random import randint

service = Service("C:\\Python\\webdriver\\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.saucedemo.com/")

try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,"user-name")))
except:
        print("login not found")

driver.find_element(By.ID, "login-button").click()

try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"error-button")))
except:
        print("no error validation")

login = driver.find_element(By.XPATH, "//h3[@data-test='error']")
login_validation = login.text
print(login_validation)
assert str(login_validation) == "Epic sadface: Username is required"

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

list_of_product = len(driver.find_elements(By.CLASS_NAME, "inventory_item_name"))
print(list_of_product)
assert int(list_of_product) == 6

value = randint(0,5)
print(value)

price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")[value]
item_price = price.text
print(item_price)

element = driver.find_elements(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")[value]
driver.execute_script("arguments[0].click();", element)

try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
except:
    print("No item in cart")

items_icon = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
items_in_cart = items_icon.get_attribute("text")
print(items_in_cart)
assert int(items_in_cart) == 1

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,"checkout")))
except:
    print("No item in cart")

cart_qty = driver.find_element(By.XPATH, "//div[@class='cart_quantity']")
cart_quantity = cart_qty.text
print(cart_quantity)
assert int(cart_quantity) == 1

cart = driver.find_element(By.CLASS_NAME, "inventory_item_price")
cart_price = cart.text
print(cart_price)
assert str(cart_price) == str(item_price)

driver.find_element(By.ID, "checkout").click()

try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,"continue")))
except:
    print("No chekout information")

driver.find_element(By.ID, "continue").click()

information = driver.find_element(By.XPATH, "//h3[@data-test='error']")
information_validation = information.text
print(information_validation)
assert str(information_validation) == "Error: First Name is required"

driver.find_element(By.ID, "first-name").send_keys("Michał")
driver.find_element(By.ID, "last-name").send_keys("Kęsicki")
driver.find_element(By.ID, "postal-code").send_keys("02-676")

driver.find_element(By.ID, "continue").click()

try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,"finish")))
except:
    print("No chekout overview")

shipping = driver.find_elements(By.CLASS_NAME, "summary_value_label")[1]
shipping_information = shipping.text
print(shipping_information)
assert str(shipping_information) == "FREE PONY EXPRESS DELIVERY!"

driver.find_element(By.ID, "finish").click()

try:
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,"back-to-products")))
except:
    print("No chekout complete")

confimation = driver.find_element(By.CLASS_NAME, "complete-header")
confirmation_information = confimation.text
print(confirmation_information)
assert str(confirmation_information) == "THANK YOU FOR YOUR ORDER"

driver.quit()