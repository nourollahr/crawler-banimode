from selenium import webdriver
from selenium.webdriver.common.by import By

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
driver.get("https://www.banimode.com/new-products?sort|discount=desc")

try:
    productsElements = driver.find_elements(By.XPATH,"//div[@id='product_list']/article")
    products = []
    for idx, item in enumerate(productsElements):
         object = {}
         object['productName'] = item.find_element(By.XPATH,"div[@class='product-card']//span[@class='product-card-name']").text
         object['productBrand'] = item.find_element(By.XPATH,"div[@class='product-card']/p/a/span[@class='product-card-brand']").text
         object['price'] = item.find_element(By.XPATH,"div[@class='product-card']//span[@class='price-disgit']").text
         object['imageHide'] = item.find_element(By.XPATH,"div[@class='product-card']//img[@class='product-card-img hover-hide']").get_attribute("src")
         object['imageShow'] = item.find_element(By.XPATH,"div[@class='product-card']//img[@class='product-card-img hover-show']").get_attribute("src")

         products.append(object)
except:
  print("An exception occurred")
finally:
    driver.quit()
