import pytest
from selenium import webdriver
@pytest.fixture(scope="session")
def setup():
   options = webdriver.ChromeOptions()
   options.add_experimental_option("detach", True)
   driver = webdriver.Chrome(options=options)
   yield driver  # Provide the driver instance to the test
   driver.quit()  # Ensure the browser is closed after the test
