# selenium_testing
using python-selenium to perform some basic and advanced testing on some of the popular websites

In this tutorial we will be using [python-selenium](https://selenium-python.readthedocs.io/) to perform some testing

First of all create a file and name it whatever you wish, I have named it 
```python_org.py```

Import the necessary python packages 

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

```

```selenium.webdriver``` is all we need to open the Firefox browser, and yes we will be 
using [Firefox](https://www.mozilla.org/en-US/firefox/new/) that works pretty fast and 
easily with selenium. Install the required ```geckodriver``` from the [docs](https://selenium-python.readthedocs.io/) or refer my [Github](https://github.com/Alexmhack/js_driven_scraping) tutorial on scraping with selenium

Finally we will be opening the python official website in Firefox browser using the 
```webdriver``` 

**python_org.py**
```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://python.org")

assert "Python" in driver.title

driver.quit()

```

```driver.get(url)``` opens the url in the browser tab. Here we are asserting 
```"Python"``` string in the title of the url we just opened using ```driver.title```

At last we ```quit()``` the driver which closes the browser window.

Now we will be performing some operations using advanced selenium methods.

##Objective
1. Open the [python.org](https://www.python.org)
2. Enter ```pycon``` in search bar of website
3. Press Enter to start search

**python_org.py**
```
elem = driver.find_element_by_name('q')
elem.clear()

elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
```

Now is the time that we use the ```Keys``` that we imported. Webdriver has a lot of 
methods that can be used for interaction with the website, one of the method is 
```get_element_by_name('q')``` which finds and returns the html element that has name 
attribute set to ```q``` ofcourse you can find any element as long it exists on the 
website.

After that we use ```clear()``` function to clear any previous or intitial values set in
the element. Then we enter ```pycon``` using ```elem.send_keys(value)``` which types in the
value inside the search form and at last we press Enter or tell to search the word 
**pycon**
