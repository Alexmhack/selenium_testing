from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://python.org")

assert "Python" in driver.title

elem = driver.get_element_by_name('q')
elem.clear()
