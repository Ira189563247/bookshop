import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_css_selector("#menu-item-50 > a").click()
mail = driver.find_element_by_id("reg_email")
mail.send_keys("until0@mail.ru")
time.sleep(5)
password = driver.find_element_by_id("reg_password")
password.send_keys("Babushka1298")
time.sleep(5)
driver.find_element_by_css_selector("div.u-column2.col-2 > form > p.woocomerce-FormRow.form-row > input.woocommerce-Button.button").click()
driver.quit()

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_css_selector("#menu-item-50 > a").click()
username = driver.find_element_by_id("username")
username.send_keys("until0@mail.ru")
time.sleep(5)
password = driver.find_element_by_id("password")
password.send_keys("Babushka1298")
time.sleep(5)
driver.find_element_by_css_selector("div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button").click()
element = driver.find_element_by_css_selector("div > div.woocommerce > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a")
element_get_text = element.text
assert element_get_text == "Logout"
driver.quit()