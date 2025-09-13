from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import speech_recognition as sr
import pyttsx3

# Initialize chatbot
bot = ChatBot('MyBot')
trainer = ListTrainer(bot)

# Train with some basic conversation
trainer.train([
    "Hi",
    "Hello! How can I help you?",
    "I have a headache",
    "How long have you had the headache?",
])

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except Exception as e:
        print("Sorry, I did not get that.")
        return ""

# Main loop
while True:
    user_input = listen()
    if user_input.lower() in ['exit', 'quit', 'bye']:
        speak("Goodbye!")
        break
    response = bot.get_response(user_input)
    print(f"Bot: {response}")
    speak(str(response))
