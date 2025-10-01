from selenium.webdriver.common.by import By
class TestCLI:
  def test_Login(self,setup):
      self.driver=setup
      self.driver.get("https://opensource-demo.orangehrmlive.com/")
      self.driver.implicitly_wait(10)
      self.driver.find_element(By.NAME, "username").send_keys("Admin")
      self.driver.find_element(By.NAME, "password").send_keys("admin123")
      self.driver.find_element(By.TAG_NAME, "button").click()  # Signin
      try:
          self.status = self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
          assert self.status == True
      except:
          assert False