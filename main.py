# Learn pyautogui
# https://www.youtube.com/watch?v=rgGDTO8g2Pg

from speak import say
from listen import listen, listenBool, wakeUpListen, listenImageGenerationPrompt
from greet import greet
from searchWeb import searchWeb
# from chat import chat
import time
from systemApps import openApp, closeApp
from datetime import datetime as dt
from onlineFunctions import weather, news, findIP, findIPLocation, findMyLocation, searchWiki, playYoutube
# from replies import randomGreet
from imageDetails import imgDetails, imageCapture
from generalFunctions import word_after_string_sequence
import pyautogui, remember, os, webbrowser
from translate import listenTranslate, translate_to_any_language
from imageGeneration import download_image

def functions():
    greet()
    while True:
        query = listen().lower()
        if "what's sleep" in query or "please sleep" in query or "go to sleep" in query:
            say(f"Ok Sir! You can call me any time, i'm just a wake up call away.")
            break
        elif "what's die" in query or "please die" in query:
            say("Bye Sir, Have a great day ahead.")
            exit()
        # elif "restart yourself" in query:
        #     say("Restarting Vats A.I.")
        #     subprocess.run(["powershell.exe", 'python -u "main.py"'])
        #     exit()
        elif "how are you" in query or "how r u" in query:
            say(f"I'm absolutely Fine sir, What about You?.")
        elif "generate image" in query:
            download_image(listenImageGenerationPrompt(), width=1280, height=720, model='flux', seed=42)
        elif "thank you" in query:
            say("Its my Plesure Sir.")
        elif "weather in" in query or "temperature in" in query:
            if "weather in" in query:
                city = word_after_string_sequence(query, "weather in")
            else:
                city = word_after_string_sequence(query, "temperature in")
            weather(city)
        elif "using artificial intelligence" in query or "using openai" in query or "using chatgpt" in query:
            searchWeb(query)
        elif "google" in query or "tell me" in query or "how to" in query or "search for" in query or "using gemini" in query or "using bard" in query or "what is" in query or "what do you mean by" in query:
            searchWeb(query)
        elif "what's the time" in query or "what is the time" in query:
            dateTime = dt.now()
            say(f"The current time is{dateTime.strftime('%I %M %p')}.")
        elif "what's the date" in query or "what is the date" in query:
            dateTime = dt.now()
            say(f"Today is{dateTime.strftime('%A %d %B %Y')}.")
        elif "open your eyes" in query or "turn on camera" in query:
            imgPath = imageCapture()
            if imgPath:
                print("Image saved successfully at:", imgPath)
            else:
                print("Capture cancelled.")
            imgDetails(imgPath)
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
        elif "open " in query:
            appName = query.replace("open ","")
            openApp(appName)
        elif "close " in query:
            appName = query.replace("close ","")
            closeApp(appName)
        elif "what's my ip" in query or "what is my ip" in query:
            findIP()
        elif "what's my location" in query or "what is my location" in query or "where am i" in query:
            findMyLocation()
        elif "find ip location" in query or "find location" in query:
            findIPLocation()
        elif "on youtube" in query:
            playYoutube(query)
        elif "on wikipedia" in query:
            searchWiki(query)
        # elif "send a mail" in query or "send an email" in query or "send mail" in query or "send email" in query:
        #     sendMail()
        elif "latest news" in query or "news" in query or "tell news" in query or "any new news" in query:
            news()
        elif "remember that" in query:
            data = query.replace("remember that", "")
            data = query.replace("Remember that", "")
            data = query.replace("Remember That", "")
            data = query.replace("remember That", "")
            data = query.replace("what's", "")
            if len(remember.data) <= 100:
                remember.data.append(data)
                say("Remembered that")
                print("Remembered that")
            else:
                say("Sorry sir i can't remember more then 100 things")
        elif "what do you remember" in query:
            rememberLen = len(remember.data)
            say(f"you asked me to remember {rememberLen} things. They are")
            for i in range(0,rememberLen):
                key=i+1
                print(remember.data[i])
                say(remember.number_names[key]+remember.data[i])
                time.sleep(0.5)
        elif "translate" in query:
            result = listenTranslate()
            if result:
                langCode, text = result
                translatedText = translate_to_any_language(text, langCode)
                print("Translated Text:", translatedText)
                say(f"The translation is: {translatedText}")
        elif "play" in query or "pause" in query:
            pyautogui.press('space')
        elif "backward" in query:
            pyautogui.press('j')
        elif "forward" in query:
            pyautogui.press('l')
        elif "captions" in query:
            pyautogui.press('c')
        elif "mute" in query:
            pyautogui.press('m')
        elif "cinema" in query:
            pyautogui.press('t')
        elif "full screen" in query:
            pyautogui.press('f')
        elif "escape" in query:
            pyautogui.press('esc')
        elif "mini player" in query:
            pyautogui.press('i')
        elif "fast" in query:
            with pyautogui.hold('shift'):
                pyautogui.press('.')
        elif "slow" in query:
            with pyautogui.hold('shift'):
                pyautogui.press(',')
        elif "next" in query:
            with pyautogui.hold('shift'):
                pyautogui.press('n')
        elif "previous" in query:
            with pyautogui.hold('shift'):
                pyautogui.press('p')
        elif "volume up" in query:
            pyautogui.press('up')
        elif "volume down" in query:
            pyautogui.press('down')
        # elif "delete temporary files" in query or "clear temporary files" in query:
        #     cwd = os.getcwd()
        #     folder1 = os.path.join(cwd+"\\Response")
        #     folder2 = os.path.join(cwd+"\\Image")
        #     folders = [folder1, folder2]
        #     for folder in folders:
        #         for fileName in os.listdir(folder):
        #             filePath = f"folder\\{fileName}"
        #             try:
        #                 if os.path.isfile(filePath) or os.path.islink(filePath):
        #                     os.remove(filePath)
        #                 # elif os.path.isdir(filePath):
        #                     # shutil.rmtree(filePath)
        #             except Exception as e:
        #                 say(f'Failed to delete {filePath}, Reason: {e}')
        #                 print(f'Failed to delete {filePath}, Reason: {e}')
        elif "shut down system" in query or "shutdown system" in query:
            say("Are you sure you want to shut down the system?")
            shutdownBool = listenBool()
            if "yes" in shutdownBool:
                say("Shuting down the system, bye sir")
                os.system("shutdown /s /t 1")
            elif "no" in shutdownBool:
                say("Shut Down Canceled")
        elif query == "":
            pass
        elif "what's die" in query or "please die" in query:
            say("Bye Sir, Have a great day ahead.")
            exit()
        else:
            searchWeb(query)

if __name__ == '__main__': 
    while True:
        query = wakeUpListen()
        print(query)
        if "wake up" in query:
            functions()
        elif "what's die" in query or "please die" in query:
            say("Bye Sir, Have a great day ahead.")
            exit()