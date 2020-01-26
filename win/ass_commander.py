import subprocess
import os
import requests
import pyttsx3
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
                self.respond(" I am Personal assistant. May i help you ? ")
            else:
                params = {"q": text}
                r = requests.get("https://www.bing.com/search", params=params)
                soup = BeautifulSoup(r.text, "html.parser")
                results = soup.find_all("div", class_="dc_mn")
                for result in results:
                    print(result.get_text())

        if "tell me about" in text:
            con = text.split(" ", 3)[-1]  # expression in python 1 equals the second word
            self.respond("Wait a minute, let me think about  " + con)
            self.respond("Ok, i got it ")
            URL = 'https://en.wikipedia.org/wiki/' + con
            content = requests.get(URL)
            soup = BeautifulSoup(content.text, 'html.parser')
            try:
                results = soup.find('div', id='mw-content-text').find('div', class_="mw-parser-output").find_all('p', limit=5)
            except:
                results = ""
            if results == "":
                self.respond("Sorry, try asking something else")
            else:
                for result in results:
                    self.respond(result.get_text().rstrip())



        if "I don't like you" in text:
            self.respond("Ok go on, i don't give a fuck!")
        if "*** you" in text:
            self.respond("So am I, fuck you triple x time")

    def respond(self, response):
        print(response)
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)    # Speed percent (can go over 100)
        engine.setProperty('volume', 0.9)  # Volume 0-1
        engine.say(response)
        engine.runAndWait()
