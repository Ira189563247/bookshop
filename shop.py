# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_css_selector("#menu-item-50 > a").click()
# username = driver.find_element_by_id("username")
# username.send_keys("until0@mail.ru")
# time.sleep(5)
# password = driver.find_element_by_id("password")
# password.send_keys("Babushka1298")
# time.sleep(5)
# driver.find_element_by_css_selector("div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button").click()
# driver.find_element_by_css_selector("#menu-item-40 > a").click()
# driver.find_element_by_css_selector("#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.outofstock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > img").click()
# element1 = driver.find_element_by_css_selector("#product-181 > div.summary.entry-summary > h1")
# element1_get_text = element1.text
# assert element1_get_text == "HTML5 Forms"
# driver.quit()


# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_css_selector("#menu-item-50 > a").click()
# username = driver.find_element_by_id("username")
# username.send_keys("until0@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Babushka1298")
# driver.find_element_by_css_selector("div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button").click()
# driver.find_element_by_css_selector("#menu-item-40 > a").click()
# driver.find_element_by_css_selector("#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a").click()
# some_element= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19.current-cat > span"),"3"))
# driver.quit()

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_css_selector("#menu-item-50 > a").click()
# username = driver.find_element_by_id("username")
# username.send_keys("until0@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Babushka1298")
# driver.find_element_by_css_selector("div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button").click()
# driver.find_element_by_css_selector("#menu-item-40 > a").click()
# sorting= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#content > form > select"),"Default sorting"))
# driver.find_element_by_css_selector("#content > form > select").click()
# driver.find_element_by_css_selector("#content > form > select > option:nth-child(6)").click()
# sorting2= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#content > form > select"),"Sort by price: high to low"))
# driver.quit()
#
#
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_css_selector("#menu-item-50 > a").click()
# username = driver.find_element_by_id("username")
# username.send_keys("until0@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Babushka1298")
# driver.find_element_by_css_selector("div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button").click()
# driver.find_element_by_css_selector("#menu-item-40 > a").click()
# driver.find_element_by_css_selector("a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()
# time.sleep(5)
# element = driver.find_element_by_css_selector("#wpmenucartli > a")
# element_get_text = element.text
# assert "1 Item" in element_get_text
# assert "₹350.00" in element_get_text
# driver.find_element_by_css_selector("#wpmenucartli > a").click()
# price= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div > div > table > tbody > tr.cart-subtotal > td"), "₹350.00"))
# totalprice= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div > div > table > tbody > tr.order-total > td"), "₹357.00"))

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_css_selector("#menu-item-50 > a").click()
username = driver.find_element_by_id("username")
username.send_keys("until0@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("Babushka1298")
driver.find_element_by_css_selector("div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button").click()
time.sleep(5)
driver.find_element_by_css_selector("#menu-item-40 > a").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector("a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()
time.sleep(5)
driver.find_element_by_css_selector("#wpmenucartli > a").click()
time.sleep(5)
button = WebDriverWait(driver, 5)
EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > div > a"))
driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div > div > div > a").click()
button1 = WebDriverWait(driver, 5)
firstname = driver.find_element_by_id("billing_first_name")
firstname.send_keys("Ira")
lastname = driver.find_element_by_id("billing_last_name")
lastname.send_keys("Irova")
phone=driver.find_element_by_id("billing_phone")
phone.send_keys("+79522754288")
driver.find_element_by_id("select2-chosen-1").click()
country=driver.find_element_by_id("s2id_autogen1_search")
country.send_keys("Hungary")
driver.find_element_by_id("select2-results-1").click()
adress=driver.find_element_by_id("billing_address_1")
adress.send_keys("Spb,Lenina street,27")
town=driver.find_element_by_id("billing_city")
town.send_keys("Spb")
zip=driver.find_element_by_id("billing_postcode")
zip.send_keys("785412")
driver.find_element_by_id("select2-chosen-2").click()
rt=driver.find_element_by_id("s2id_autogen2_search")
rt.send_keys("Vas")
time.sleep(5)
driver.find_element_by_id("select2-results-2").click()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
driver.find_element_by_id("payment_method_cheque").click()
time.sleep(5)
driver.find_element_by_id("place_order").click()
time.sleep(5)
some_element= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.woocommerce > p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
some_element= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > table > tfoot > tr:nth-child(3) > td"), "Check Payments"))
driver.quit()

