from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import pyttsx3
import speech_recognition as sr
import pytz
import subprocess
import random
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk
# from selftraining import bot


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february","march","april","may","june","july","august","september","october","november","december"]
DAYS = ["monday", "tuesday","wednesday", "thursday", "friday","saturday","sunday"]
DAY_EXTENTIONS = ["rd","th","st", "nd"]

#getting text file and conveting it to speech by saving the text as mp3.
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id) 
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

#getting inputs from the user through the computer Microphone.
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()

#authenticating into google acount getting the asked events. 


#The function to train the model

#naming the chatbot.
