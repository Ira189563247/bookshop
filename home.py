from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.button.product_type_simple.ajax_add_to_cart").click()
driver.find_element_by_css_selector("#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab > a").click()
driver.find_element_by_css_selector("#commentform > p.comment-form-rating > p > span > a.star-5").click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
author = driver.find_element_by_id("author")
comment.send_keys("Nora")
male = driver.find_element_by_id("email")
comment.send_keys("until0@mail.ru")
driver.find_element_by_id("submit").click()
driver.quit()
