# import webdriver
from selenium import webdriver
 
# create webdriver object
driver = webdriver.Firefox()
 
 
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
 
# get element
element = driver.find_element_by_name("search")
 
# send keys
element.send_keys("Arrays")
