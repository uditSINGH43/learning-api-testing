import pytest
from selenium import webdriver
class TestTitle:
   def test_title_chrome(self):
       opt = webdriver.ChromeOptions()
       opt.add_experimental_option("detach", True)
       driver = webdriver.Chrome(options=opt)
       driver.get("https://www.google.com/")
       act_title = driver.title
       exp_title = "Google"
       if act_title == exp_title:
           print("Test passed")
       else:
           print("Test Failed")
       assert act_title == exp_title  # validation
       driver.quit()
   def test_title_edge(self):
       opt = webdriver.EdgeOptions()
       opt.add_experimental_option("detach", True)
       driver = webdriver.Edge(options=opt)
       driver.get("https://www.google.com/")
       act_title = driver.title
       exp_title = "Google"
       if act_title == exp_title:
           print("Test passed")
       else:
           print("Test Failed")
       assert act_title == exp_title  # validation
       driver.quit()
   def test_title_firefox(self):
       opt = webdriver.FirefoxOptions()
       driver = webdriver.Firefox(options=opt)
       driver.get("https://www.google.com/")
       act_title = driver.title
       exp_title = "Google"
       if act_title == exp_title:
           print("Test passed")
       else:
           print("Test Failed")
       assert act_title == exp_title  # validation
       driver.quit()