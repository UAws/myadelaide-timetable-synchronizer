from selenium.webdriver.support import expected_conditions
from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
