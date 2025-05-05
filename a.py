import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Capture audio from microphone
with sr.Microphone() as source:
    print("🎤 Say something:")
    audio = r.listen(source)

# Convert speech to text
try:
    text = r.recognize_google(audio)
    print("📝 You said:", text)
except sr.UnknownValueError:
    print("❌ Could not understand audio.")
except sr.RequestError:
    print("⚠️ Could not request results; check your internet connection.")
    

