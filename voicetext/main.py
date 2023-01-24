from gtts import gTTS 
import os
file = open("Тут название файла в одной директории с кодом", "r").read()

speech = gTTS(text=file, lang='ru', slow=False)
speech.save("voice.mp3")
os.system("voice.mp3")