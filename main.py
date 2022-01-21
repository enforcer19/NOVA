import pyttsx3 as p
import speech_recognition as sr
import wolframalpha
from YT_auto import music
from selenium_web_driver import inforr
from News import *
import randfacts
from pyjokes import *
from weather import *
import datetime
from search import sear
import random2
import math
import warnings
import open
import os
import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


warnings.filterwarnings("ignore")

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return ("Morning")
    elif hour >= 12 and hour < 16:
        return ("Afternoon")
    elif hour >= 16 and hour < 19:
        return ("evening")
    else:
        return ("night")

def quitApp():
    hour = int(datetime.datetime.now().hour)
    if hour >= 3 and hour < 18:
        print("have a good day sir")
        speak("have a good day sir")
    else:
        print("Goodnight sir")
        speak("Goodnight sir")
    print("Offline")
    exit(0)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

#flags
Light_status_flag = False


today_date = datetime.datetime.now()
r = sr.Recognizer()
speak("Tell the wake up word")
wake = "hello Nova"
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening")
    audio = r.listen(source)
    wakeword = r.recognize_google(audio)
    print(wakeword)
if wake == wakeword:
    while True:
        speak("hello sir, good " + wishme() + ", i'm here to assist you.")
        speak("How are you")

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("Listening")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)

        if "what" and "about" and "you" in text:
            speak("I am also having a good day")

        if __name__ == "__main__":
            while True:
                speak("What can i do for you??")

                with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source, 1.2)
                        print('Listening.....')
                        audio = r.listen(source)
                        text2 = r.recognize_google(audio)


                if "information" in text2:
                    speak("You need information related to which topic")

                    with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source, 1.2)
                        print('Listening.....')
                        audio = r.listen(source)
                        infor = r.recognize_google(audio)
                    speak("Searching {} in wikipedia".format(infor))
                    print("Searching {} in wikipedia".format(infor))
                    assist = inforr()
                    assist.get_info(infor)

                elif "play" and "video" in text2:
                    speak("Which video you want me to play??")

                    with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source, 1.2)
                        print('Listening.....')
                        audio = r.listen(source)
                        vid = r.recognize_google(audio)
                    speak("Playing {} on youtube".format(vid))
                    print("Playing {} on youtube".format(vid))
                    assist = music()
                    assist.play(vid)

                elif "news" in text2:
                    speak("Sure sir, Now I will read news for you")
                    arr = news()
                    for i in range(len(arr)):
                        print(arr[i])
                        speak((arr[i]))

                elif "temperature" in text2:
                    speak("Temperature in Chennai is" + str(temp()) + " degree celcius" + " and with " + str(des()))
                    print("Temperature in Chennai is" + str(temp()) + " degree celcius" + " and with " + str(des()))

                elif "funny" in text2:
                    speak("Get ready for some chuckles")
                    joke = pyjokes.get_joke()
                    speak(joke)
                    print(joke)

                elif "your name" in text2:
                    speak("My name is Next genn Optimal Voice Assistant Nova")

                elif "fact" in text2:
                    speak("Sure sir , ")
                    x = randfacts.getFact()
                    speak("Did you know that," + x)
                    print(x)

                elif "search" in text2:
                    speak("What should i search for sir")
                    with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source, 1.2)
                        print('Listening.....')
                        audio = r.listen(source)
                        searc = r.recognize_google(audio)
                    speak("Searching {} in Google".format(searc))
                    print("Searching {} in Google".format(searc))
                    asist = sear()
                    asist.get_infoo(searc)


                elif "game" in text2:
                    speak("enter your lower limit sir")
                    with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source, 1.2)
                        print('Listening.....')
                        audio = r.listen(source)
                        lower = int(r.recognize_google(audio))
                    speak("now, Enter your upper limit")
                    with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source, 1.2)
                        print('Listening.....')
                        audio = r.listen(source)
                        upper = int(r.recognize_google(audio))
                    x = random2.randint(lower, upper)
                    speak("\n\tYou've only " + str(round(math.log(upper - lower + 1, 2))) + " chances to guess the integer!\n")
                    print("\n\tYou've only " + str(round(math.log(upper - lower + 1, 2))) + " chances to guess the integer!\n" + str(upper), str(lower))
                    count = 0
                    while count < math.log(upper - lower + 1, 2):
                        count += 1
                        speak("start guessing")
                        speak("Guess a number")
                        with sr.Microphone() as source:
                            r.energy_threshold = 10000
                            r.adjust_for_ambient_noise(source, 1.2)
                            print('Listening.....')
                            audio = r.listen(source)
                            guess = int(r.recognize_google(audio))
                        if x == guess:
                            print("Congratulations you did it in " + str(count) + " try")
                            speak("Congratulations you did it in " + str(count) + " try")
                            break
                        elif x > guess:
                            print("You guessed too small!")
                            speak("You guessed too small!")
                        elif x < guess:
                            print("You Guessed too high!")
                            speak("You Guessed too high!")
                    if count >= math.log(upper - lower + 1, 2):
                        print("\nThe number is %d" % x)
                        speak("\nThe number is %d" % x)
                        print("\tBetter Luck Next time!")
                        speak("\tBetter Luck Next time!")

                elif "reboot the system" in text2:
                    speak("Do you wish to restart your computer ?")
                    with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source, 1.2)
                        print('Listening.....')
                        audio = r.listen(source)
                        restart = r.recognize_google(audio)
                    if restart == 'no':
                        exit()
                    else:
                        os.system("shutdown /r /t 1")

                elif "open" in text2:
                    speak("What should i open sir ??")
                    with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source, 1.2)
                        print('Listening.....')
                        audio = r.listen(source)
                        pen = r.recognize_google(audio)
                    speak("opening your {}".format(pen))
                    ipen = open.open_thing()
                    ipen.open_things(pen)

                elif "date" in text2:
                    speak("Today is " + today_date.strftime("%d") + " of" + today_date.strftime(
                        "%B") + ", And it's currently " + today_date.strftime("%I") + today_date.strftime(
                        "%M") + today_date.strftime("%p"))
                    print("Today is " + today_date.strftime("%d") + " of" + today_date.strftime(
                        "%B") + ", And it's currently " + today_date.strftime("%I") + today_date.strftime(
                        "%M") + today_date.strftime("%p"))

                elif "calculate" in text2:
                    app_id = "RVX3AG-5RTPKWW3KQ"
                    client = wolframalpha.Client(app_id)
                    indx = text2.lower().split().index('calculate')
                    query = text2.split()[indx + 1:]
                    res = client.query(' '.join(query))
                    answer = next(res.results).text
                    print("The answer is " + answer)
                    speak("The answer is " + answer)

                elif "light on" in text2:
                        #if Light_status_flag == False:
                            cmd = "ON"
                            Status = write_read(cmd) # expected output from arduino is "STATE:Light:ON"
                            speak("Lights are turned on")
                       # elif Light_status_flag == True:
                           # speak("Lights are already ON")


                elif "light off" in text2:
                        #if Light_status_flag == True:
                        cmd = "OFF"
                        Status = write_read(cmd)
                        speak("Lights are turned off")
                        #elif Light_status_flag == False:
                          #  speak("Lights are already off")

                elif "stop" or "exit" or "end" in text2:
                    speak("It's a pleasure helping you and I am always here to help you out!")
                    quitApp()