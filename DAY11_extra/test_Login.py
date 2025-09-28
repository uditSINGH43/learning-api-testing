from selenium.webdriver.common.by import By
class TestLogin:
   def test_Login(self, setup):
       self.driver = setup
       self.driver.get("https://opensource-demo.orangehrmlive.com/")
       self.driver.implicitly_wait(10)
# Enter username and password
       self.driver.find_element(By.NAME, "username").send_keys("Admin")
       self.driver.find_element(By.NAME, "password").send_keys("admin123")
# Click the Signin button
       self.driver.find_element(By.TAG_NAME, "button").click()
# Validate login success
       try:
           self.status = self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
           assert self.status is True
       except:
           assert False
