from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.youtube.com")
assert "YouTube" in driver.title
elem = driver.find_element(By.NAME, "search_query")
elem.clear()
elem.send_keys("aamatimro maya smriti band")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()