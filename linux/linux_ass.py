import pyaudio
import wave
import speech_recognition as sr
import subprocess
from ass_comander import Commander
import sys
import pyttsx3

running = True

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


play_audio("../audio/intro.wav")

r = sr.Recognizer()
cmd = Commander()


def initspeech():
    # One time initialization
    engine = pyttsx3.init()

    # Set properties _before_ you add things to say
    engine.setProperty('rate', 120)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Queue up things to say.
    # There will be a short break between each one
    # when spoken, like a pause between sentences.
    engine.say("I am Listening ")
    engine.runAndWait()
    print("Say something, I am Listening ..")

    with sr.Microphone() as source:
        print("Say something ..")
        audio = r.listen(source)

    play_audio("../audio/and.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        engine.say("Sorry, could you say it again ? ")
        engine.runAndWait()
        print("Sorry, could you say it again ?")

    print("Your command :")
    print(command)
    if command in ["stop right now", "see you later", "see yaa", "see ya later", "bye", "bye-bye", "goodbye"]:
        global running
        running = False
        print("Stopping ...")
        play_audio("../audio/bye-bye.wav")
        sys.exit()
    cmd.discover(command)



while running:
    initspeech()

