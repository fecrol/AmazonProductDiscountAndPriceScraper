from WebdriverConfig import WebdriverConfig
from pages.CookiePreferences import CookiePreferences
from pages.ProductPage import ProductPage
from datetime import datetime

from utilities.CsvWriter import CsvWriter

url = "https://www.amazon.co.uk/Logitech-Rechargeable-Multi-Device-Programmable-Productivity/dp/B071KZS3MF/ref=sr_1_5?crid=2D1EPUCESTOID&keywords=logitech+mx+master&qid=1659795024&sprefix=logitech+mx+master%2Caps%2C840&sr=8-5"

webdriver_config = WebdriverConfig()

driver = webdriver_config.start_driver()

driver.get(url)

cookie_preferences_page = CookiePreferences(driver)
cookie_preferences_page.click_accept_cookies_btn()

product_page = ProductPage(driver)
savings_percentage = product_page.get_savings_percentage()
savings_percentage = savings_percentage.replace("-", "").replace("%", "")

price_to_pay = product_page.get_price_to_pay()
price_to_pay = ".".join(price_to_pay.split("\n")).replace("£", "")

date = datetime.today().strftime("%Y-%m-%d")

csv_filename = "price_data.csv"
data = [[date, savings_percentage, price_to_pay]]
columns = ["Date", "Discount Percentage", "Current Price"]

csv_writer = CsvWriter()
csv_writer.append_to_csv(csv_filename, data, columns)

driver.quit()
