from gtts import gTTS
import os

with open("output/script.txt") as f:
    script = f.read()

tts = gTTS(script, lang='en')
tts.save("output/voice.mp3")

print("✅ Voiceover generated successfully.")
