import subprocess
import os
import requests
from bs4 import BeautifulSoup


class Commander:
    def __init__(self):
        self.confirm = ["yes", "ok", "go on", "sure", "do it", "yeah", "yaa", "Imm", "confirm", "of course"]
        self.cancel = ["nope", "no", "noo", "not yet", "don't", "do not", "stop", "wait", "hold on", "not now"]

    def discover(self, text):
        if "what" in text:
            if "my name" in text:
                self.respond("You haven't told me your name yet")
            if "your name" in text:
                self.respond(" I am Python 3.7.2 2019 released version ..")
            else:
                params = {"q": text}
                r = requests.get("https://www.bing.com/search", params=params)
                soup = BeautifulSoup(r.text, "html.parser")
                results = soup.find_all("div", class_="dc_mn")
                for result in results:
                    print(result.get_text())

        if "tell me about" in text:
            con = text.split(" ", 3)[-1]  # expression in python 1 equals the second word
            self.respond("Searching for " + con)
            URL = 'https://en.wikipedia.org/wiki/' + con
            content = requests.get(URL)
            soup = BeautifulSoup(content.text, 'html.parser')

            results = soup.find('div', id='mw-content-text')
            for table in results.find_all("table"):
                table.extract()
            for style in results.find_all("style"):
                style.extract()
            print(results.get_text())

    def respond(self, response):
        print(response)
        subprocess.call("echo " + response, shell=True)
