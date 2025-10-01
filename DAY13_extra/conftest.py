import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser):
  if browser == "chrome":
      options = webdriver.ChromeOptions()
      options.add_experimental_option("detach", True)
      driver = webdriver.Chrome(options=options)
  elif browser == "edge":
      options = webdriver.EdgeOptions()
      options.add_experimental_option("detach", True)
      driver = webdriver.Edge(options=options)
  elif browser == "firefox":
      options = webdriver.FirefoxOptions()
      driver = webdriver.Firefox(options=options)
  yield driver  # Provide the driver instance to the test
  driver.quit()  # Ensure the browser is closed after the test


def pytest_addoption(parser):
   parser.addoption(
       "--browser",
       action="store",
       default="chrome",
       help="Browser to run tests against"
   )
@pytest.fixture
def browser(request):
   return request.config.getoption("--browser")

@pytest.mark.optionalhook
def pytest_metadata(metadata):
   metadata.pop("Python", None)
   metadata.pop("Plugins", None)

@pytest.mark.optionalhook
def pytest_configure(config):
   config.stash[metadata_key]['Project Name'] = 'Orange HRM'
   config.stash[metadata_key]['Module Name'] = 'Login Module'
   config.stash[metadata_key]['Tester Name'] = 'Udit'
   config.stash[metadata_key]['Platform'] = 'safari'
