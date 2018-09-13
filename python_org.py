from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://python.org")

assert "Python" in driver.title

driver.quit()
