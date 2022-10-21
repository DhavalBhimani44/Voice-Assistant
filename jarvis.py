import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
import time
import random
import pyjokes
import sys
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"Good Morning Sir, it's {tt} ")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon Sir, it's {tt}")

    else:
        speak(f"Good Evening Sir, it's {tt}")
    speak("How can I help you?")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

# def waking():
#     voicepath = 'C:\\Users\\Dhaval\\PycharmProjects\\pythonProject\\Hey Jarvis.pmdl
#     os.startfile(voicepath)


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

# to open anything
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            #print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Sir, What should I search on Google?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            speak("Ok Sir,Playing music!")
            os.startfile(os.path.join(music_dir, songs[6]))

        elif 'play random music' in query:
            speak("ok sir finding some random music")
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'ip address' in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")

        elif 'fifa' in query:
            fpath = 'E:\\FIFA18\\FIFA18.exe'
            os.startfile(fpath)

        elif 'tell me more about you' in query:
            speak("I'm JARVIS sir!I was made me on 22nd November, 2020!I'm Mr. Dhaval's personal assistant!")

        elif 'open chrome' in query:
            gcpath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            speak("Opening Google Chrome")
            os.startfile(gcpath)

        elif 'close chrome' in query:
            speak("Ok Sir, closing Google Chrome")
            os.system("taskkill /f /im chrome.exe")

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'you can sleep' in query:
            speak("Thank you sir for using me, Have a good day")
            sys.exit()

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "weather" in query:
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            webbrowser.open("https://www.accuweather.com/en/in/" + city_name + "/202440/weather-forecast/202440")
            speak("Opening weather for")
            speak(city_name)

        elif 'new tab' in query:
            speak("Opening new tab!")
            pyautogui.hotkey('ctrl', 't')

        elif 'close tab' in query:
            speak("Closing tab!")
            pyautogui.hotkey('ctrl', 'w')

        elif 'close window' in query:
            speak("Closing window!")
            pyautogui.hotkey('alt', 'f4')

        elif 'i want to search' in query or 'write' in query:

            speak("Ok sir, Please say what you want to write or search")
            s = takeCommand()
            pyautogui.write(s)
            time.sleep(3)
            pyautogui.press('enter')

        elif 'up' in query:
            pyautogui.press('up')

        elif 'down' in query:
            pyautogui.press('down')

        elif 'left' in query:
            pyautogui.press('left')

        elif 'right' in query:
            pyautogui.press('right')

        elif 'enter' in query:
            pyautogui.press('enter')

        elif 'i want to search' in query or 'write' in query:
            speak("Ok sir please say what you want to write or search sir")
            s = takeCommand()
            pyautogui.write(s)
            time.sleep(2)
            pyautogui.press('enter')

        elif 'open brave' in query:
            gcpath = '"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk"'
            speak("Opening Brave Browser")
            os.startfile(gcpath)