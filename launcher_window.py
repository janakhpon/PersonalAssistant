import subprocess
import os


class Commander:
    def __init__(self):
        self.confirm = ["yes", "ok", "go on", "sure", "do it", "yeah", "yaa", "Imm", "confirm", "of course"]
        self.cancel = ["nope", "no", "noo", "not yet", "don't", "do not", "stop", "wait", "hold on", "not now"]

    def discover(self, text):
        if "launch code" or "open code" in text:
            app = text.split(" ", 1)[-1]  # expression in python 1 equals the second word
            self.respond("Opening " + app)
            if app == "notepad":
                
                pdf = "path/to/pdf"
                acrobatPath = r'C:\Program Files\Adobe\Reader 9.0\Reader\AcroRd32.exe'
                subprocess.Popen("%s %s" % (acrobatPath, pdf))

    def respond(self, response):
        print(response)
        subprocess.call("echo " + response, shell=True)
