import speech_recognition as sr
import nltk
from gtts import gTTS
import pyttsx3
import os
import time

# Initialize chatbot
chatbot = ChatBot('Assistant')
trainer = ChatterBotCorpusTrainer(chatbot)

# Train chatbot on English corpus
trainer.train("chatterbot.corpus.english")

# Function to get response from chatbot
def get_response(command):
    return str(chatbot.get_response(command)
               
# Function to execute command
def execute_command(command):
    if 'time' in command:
        current_time = time.ctime()
        text_to_speech(current_time)
    else:
        response = get_response(command)
        text_to_speech(response)

# Function to convert text to speech
def text_to_speech(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""

# Main function
def main():
    while True:
        command = recognize_speech()
        if command.lower() in ["stop", "bye"]:
            print("Stopping...")
            break
        execute_command(command)

if __name__ == "__main__":
    main()