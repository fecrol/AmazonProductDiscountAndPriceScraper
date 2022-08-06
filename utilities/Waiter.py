from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Waiter():
    
    def wait_for_element_to_be_clickable(self, driver, seconds, element):

        webdriver_wait = WebDriverWait(driver, timeout=seconds)
        webdriver_wait.until(expected_conditions.element_to_be_clickable(element))