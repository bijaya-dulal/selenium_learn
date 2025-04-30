# #Using selenium to write test
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# class PythonOrgSearch(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox()
      

#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element(By.NAME, "q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         self.assertNotIn("No results found.", driver.page_source)


#     def tearDown(self):
#         self.driver.close()  

# if __name__ == "__main__":
#     unittest.main()

# Using Selenium with remote WebDriver

from selenium import webdriver

# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    options=webdriver.ChromeOptions()
# )

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   options=webdriver.FirefoxOptions()
)

driver.get("http://www.youtube.com")
assert "YouTube" in driver.title
elem = driver.find_element(By.NAME, "search_query")
elem.clear()
elem.send_keys("aamatimro maya smriti band")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source