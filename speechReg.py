import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Define the audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

# Perform speech recognition on the audio source
try:
    text = r.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError:
    print("Sorry, my speech recognition service is currently unavailable.")

