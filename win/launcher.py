import subprocess
import os


class Commander:
    def __init__(self):
        self.confirm = ["yes", "ok", "go on", "sure", "do it", "yeah", "yaa", "Imm", "confirm", "of course"]
        self.cancel = ["nope", "no", "noo", "not yet", "don't", "do not", "stop", "wait", "hold on", "not now"]

    def discover(self, text):
        if "launch" or "open" in text:
            app = text.split(" ", 1)[-1]  # expression in python 1 equals the second word
            self.respond("Opening " + app)
            if app == "notepad":
                acrobatPath = r'C:\Windows\system32\notepad.exe'
                # subprocess.run(['notepad.exe', 'test.txt'])
                os.system('"C://Temp/a b c/Notepad.exe"')


    def respond(self, response):
        print(response)
        subprocess.call("echo " + response, shell=True)
