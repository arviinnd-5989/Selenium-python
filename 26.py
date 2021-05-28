# import webdriver
from selenium import webdriver
  
# create webdriver object
driver = webdriver.Firefox()
  
# get geeksforgeeks.org
driver.get("https://www.google.co.in/")
  
# get geeksforgeeks.org
driver.get("https://www.google.com/")
  
# one step backward in browser history
driver.back()
  
# one step backward in browser history
driver.forward()
