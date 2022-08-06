from seleniumpagefactory.Pagefactory import PageFactory
from utilities.Waiter import Waiter

class ProductPage(PageFactory, Waiter):

    def __init__(self, driver):

        self.driver = driver
    
    locators = {
        "savings_percentage": ("css", ".savingsPercentage"),
        "add_to_cart_btn": ("id", "add-to-cart-button")
    }

    def get_savings_percentage(self):

        try:
            self.wait_for_element_to_be_clickable(self.driver, 5, self.add_to_cart_btn)
            return self.savings_percentage.text
        except:
            return "0%"