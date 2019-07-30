import subprocess
import os


class Commander:
    def __init__(self):
        self.confirm = ["yes", "ok", "go on", "sure", "do it", "yeah", "yaa", "Imm", "confirm", "of course"]
        self.cancel = ["nope", "no", "noo", "not yet", "don't", "do not", "stop", "wait", "hold on", "not now"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "what my name" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is Python 3.7.2. May I help you?")

        if "launch code" or "open code" in text:
            app = text.split(" ", 1)[-1]  # expression in python 1 equals the second word
            self.respond("Opening " + app)
            if app == "notepad":
                subprocess.call('C:\Windows\system32\notepad.exe')

    def respond(self, response):
        print(response)
        subprocess.call("echo " + response, shell=True)
