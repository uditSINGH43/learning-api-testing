import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClass:
   @pytest.mark.parametrize('user,pwd',
                            [("Admin", "admin123"),
                             ("adm", "admin123"),
                             ("Admin", "adm"),
                             ("adm", "adm")
                             ])
   def test_Login(self, user, pwd):
       options = webdriver.ChromeOptions()
       options.add_experimental_option("detach", True)
       self.driver = webdriver.Chrome(options=options)
       self.driver.get("https://opensource-demo.orangehrmlive.com/")
       self.driver.implicitly_wait(10)
       self.driver.find_element(By.NAME, "username").send_keys(user)
       self.driver.find_element(By.NAME, "password").send_keys(pwd)
       self.driver.find_element(By.TAG_NAME, "button").click()  # Signin
       try:
           self.status = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").is_displayed()
           self.driver.close()
           assert self.status == True
       except:
           self.driver.close()
           assert False