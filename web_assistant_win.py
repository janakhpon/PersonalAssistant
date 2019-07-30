import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys


class Fetcher:
    def __init__(self, url):

        # prepare the option for the chrome driver
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        # start chrome browser
        self.driver = webdriver.Chrome(options=options)
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url
        print(self.url)

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "gsfi")
            ))
        except:
            print("Failed")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        answer = soup.find_all(class_="_sPg")[0]
        print(answer.get_text())
        return answer.get_text()
