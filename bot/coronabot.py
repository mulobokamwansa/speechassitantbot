#!/usr/bin/python3
import os
import aiml
from chatbot import *




BRAIN_FILE="brain.dump"
k = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as aC:\Users\Mukoma\Music\coronabot-coronavirus-chatbot-master\\chatbot.py
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files

if os.path.exists(BRAIN_FILE):
    print(BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    speak("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    speak(BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

    # Endless loop which passes the input to the bot and prints
    # its response

        