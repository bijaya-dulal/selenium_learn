#interacting with the page 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
##this is how we select the element 
# element = driver.find_element(By.ID, "passwd-id")
# element = driver.find_element(By.NAME, "passwd")
# element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
# element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")


##THIS WILL SEND THE TEXT TO INTERACT
#element.send_keys("some text")

##this clear the input field
#element.clear()

# #filling the forms
# element = driver.find_element(By.XPATH, "//select[@name='name']")
# all_options = element.find_elements(By.TAG_NAME, "option")
# for option in all_options:
#     print("Value is: %s" % option.get_attribute("value"))
#     option.click()
 ##this is  not a good for selection for the option because the all option are slecting 

##we can use Select class to  work with the select input tags


# from selenium.webdriver.support.ui import Select
# select = Select(driver.find_element(By.NAME, 'name'))
# select.select_by_index(index)
# select.select_by_visible_text("text")
# select.select_by_value(value)


## this is for deselection of the selected options
#select.deselect_all()


