from WebdriverConfig import WebdriverConfig
from pages.CookiePreferences import CookiePreferences
from pages.ProductPage import ProductPage
from datetime import datetime
from utilities.CsvWriter import CsvWriter
from utilities.CliArgumentParser import CliArgumentParser
import os

cli_argument_parser = CliArgumentParser()

url = cli_argument_parser.get_url()
date = datetime.today().strftime("%Y-%m-%d")
csv_file_path = cli_argument_parser.get_csv_file_path()
csv_filename = cli_argument_parser.get_csv_filename()

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

data = [[date, savings_percentage, price_to_pay]]
columns = ["Date", "Discount Percentage", "Current Price"]

os.chdir(csv_file_path)

csv_writer = CsvWriter()
csv_writer.append_to_csv(csv_filename, data, columns)

driver.quit()
