import pyaudio
import wave
import speech_recognition as sr
import subprocess
from audio_cmd_window import Commander
import sys

running = True


def say(text):
    subprocess.call('say ' + text, shell=True)


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


play_audio("./audio/intro.wav")

r = sr.Recognizer()
cmd = Commander()


def initspeech():
    print("Listening ..")
    play_audio("./audio/yes.wav")

    with sr.Microphone() as source:
        print("Say something ..")
        audio = r.listen(source)

    play_audio("./audio/and.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        play_audio("./audio/blah-blah-blah.wav")
        print("couldn't understand you")

    print("Your command :")
    print(command)


initspeech()
