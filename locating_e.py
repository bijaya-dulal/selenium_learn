## this are the methods to select the element

# from selenium.webdriver.common.by import By

# driver.find_element(By.XPATH, '//button[text()="Some text"]')
# driver.find_elements(By.XPATH, '//button')

##the attributes that can be use with BY class

# ID = "id" #loacte by the id attributes
# NAME = "name" #locate by the name
# XPATH = "xpath" #locate by x path , navigate the DOM for example
 #driver.find_element(By.XPATH, "//input[@type='submit']") #this will locate the input element with type submit

# LINK_TEXT = "link text" # locate anchor by the exact visible text for example
# diver.find_element(By.LINK_TEXT,'home')

# PARTIAL_LINK_TEXT = "partial link text" #same as the  LINK_TEXT partial match will be okay.


# TAG_NAME = "tag name" #locate by the tag name
# CLASS_NAME = "class name" #by class name
# CSS_SELECTOR = "css selector" #use css selector

#find_element will return the single first come element and elements give te list of the element

##


