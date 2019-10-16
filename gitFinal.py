#! /usr/bin/env python3

from wikipedia import summary, DisambiguationError, random
import pyttsx3
from multiprocessing import Process
import warnings

warnings.filterwarnings("ignore")
UserID = ''

with open("Exit.txt",'r') as f:
    data = f.read()
    ExitCommands = data.split(',')

# initializing TTS Engine
bot = pyttsx3.init()
rate = bot.getProperty('rate')
bot.setProperty('rate', rate-35)
bot.setProperty('volume', 1.0)

def AnswerQuery(Query):
    search = Query
    try:
        result = summary(search,sentences=5,auto_suggest=True)
        bot.say("Here's what I found on" + Query )
    except DisambiguationError as e:
        result = "Please make your Query specific"
    finally:
        bot.say(result)
        bot.runAndWait()

def StartUp():
    global UserID

    bot.say('Hi')
    bot.say("I am Athena, a virtual assistant. What's your name ")
    bot.runAndWait()
    UserID = str(input("Enter Name: "))
    bot.say("Nice to meet you "+ UserID)
    bot.runAndWait()

def Random():
    result = summary(random(), sentences=4)
    bot.say(result)
    bot.runAndWait()

def ShutDown():
    global UserID

    bot.say("Bye " + UserID)
    bot.runAndWait()
    bot.stop()

def Intro():
    bot.say("I can look up phrases, or tell you about random things. type random to try it")
    bot.runAndWait()

if __name__ == "__main__":
    StartUp()
    Intro()
    Question = ''
    while True:
        bot.say("What can i look up for you")
        bot.runAndWait()
        Question = (input("Enter Query: ")).lower()
        if Question in ExitCommands:
            break
        if Question == "random":
            Random()
        else:
            AnswerQuery(Question)
    ShutDown()