from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebdriverConfig:

    def __init__(self):
        
        self.__chrome_service = Service(executable_path=ChromeDriverManager().install())
        self.__options = webdriver.ChromeOptions()
        self.__options.add_argument('--log-level=1')
        self.__options.headless = True
        self.__driver = None
    
    def start_driver(self):

        self.__driver = webdriver.Chrome(service=self.__chrome_service, options=self.__options)

        return self.__driver