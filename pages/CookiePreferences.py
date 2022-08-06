from seleniumpagefactory.Pagefactory import PageFactory

from utilities.Waiter import Waiter

class CookiePreferences(PageFactory, Waiter):

    def __init__(self, driver):
        
        self.driver = driver
    
    locators = {
        "accept_cookies_btn": ("id", "sp-cc-accept")
    }

    def click_accept_cookies_btn(self):

        self.wait_for_element_to_be_clickable(self.driver, 5, self.accept_cookies_btn)
        self.accept_cookies_btn.click()
