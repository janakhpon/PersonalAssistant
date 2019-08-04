import subprocess
import os
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys


class Commander:
    def __init__(self):
        self.confirm = ["yes", "ok", "go on", "sure", "do it", "yeah", "yaa", "Imm", "confirm", "of course"]
        self.cancel = ["nope", "no", "noo", "not yet", "don't", "do not", "stop", "wait", "hold on", "not now"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my name" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is Python 3.7.2. May I help you?")
        else:
            # prepare the option for the chrome driver
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            # start chrome browser
            driver = webdriver.Chrome(options=options)
            driver.wait = WebDriverWait(driver, 5)
            url = "https://www.google.com/search?q=" + text
            print(url)
            driver.get(url)
            try:
                ip = driver.wait.until(EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "Z0LcW")
                ))
            except:
                print("Failed")

            soup = BeautifulSoup(driver.page_source, "html.parser")
            answer = soup.find_all(class_="_Z0LcW")
            self.respond(answer)
            if not answer:
                answer = soup.find_all(class_="_m3b")
                self.respond(answer)

            if not answer:
                answer = "I don't know."
                self.respond(answer)

            driver.quit()
            self.respond(answer[0].get_text())

    def respond(self, response):
        print(response)
        subprocess.call("echo " + response, shell=True)
