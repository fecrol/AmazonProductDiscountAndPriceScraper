from seleniumpagefactory.Pagefactory import PageFactory

class CookiePreferences(PageFactory):

    def __init__(self, driver):
        
        self.driver = driver
    
    locators = {
        "accept_cookies_btn": ("id", "sp-cc-accept")
    }

    def click_accept_cookies_btn(self):
        self.accept_cookies_btn.click()
