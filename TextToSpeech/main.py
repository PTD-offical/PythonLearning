from gtts import gTTS
import os

# Text in Arabic
text = "بحبك يا امي"
language = "ar"

# Creating speech object
speech = gTTS(text=text, lang=language, slow=False)
speech.save("output.mp3")

# Play the audio file (make sure you have a player installed)
os.system("vlc output.mp3")
