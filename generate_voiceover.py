import pyttsx3

engine = pyttsx3.init()
with open("output/script.txt") as f:
    script = f.read()

engine.save_to_file(script, "output/voice.mp3")
engine.runAndWait()
