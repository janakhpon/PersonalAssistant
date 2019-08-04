import subprocess
import os
import requests
from bs4 import BeautifulSoup
from web_assistant_win import Fetcher


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
            f = Fetcher("https://www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)
            print(answer)

    def respond(self, response):
        print(response)
        subprocess.call("echo " + response, shell=True)
