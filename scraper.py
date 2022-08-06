from WebdriverConfig import WebdriverConfig
import time

url = "https://www.amazon.co.uk/Logitech-Rechargeable-Multi-Device-Programmable-Productivity/dp/B071KZS3MF/ref=sr_1_5?crid=2D1EPUCESTOID&keywords=logitech+mx+master&qid=1659795024&sprefix=logitech+mx+master%2Caps%2C840&sr=8-5"

webdriver_config = WebdriverConfig()

driver = webdriver_config.start_driver()

driver.get(url)

time.sleep(2)

driver.quit()
