from gtts import gTTS

with open("output/script.txt", "r", encoding="utf-8") as f:
    script = f.read()

tts = gTTS(text=script, lang="te", slow=False)
tts.save("output/voiceover.mp3")
