import speech_recognition as sr
from speak import say
from replies import randomReply

def listenBool():
    while True:
        r = sr.Recognizer()
        with sr.Microphone(device_index=2) as source:
            print("Listining...")
            r.pause_threshold = 1
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1)
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            return str(query).lower()
        except Exception as e:
            say(f"Sorry sir, I Couldn't understand, Can you please repeat.")

def listen():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listining...")
        r.pause_threshold = 1
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        # else:
        #     say(choice(random_reply))
    except Exception as e:
        say(f"Sorry sir, I Couldn't understand, Can you please repeat.")
        # print(f"Sorry sir, I Couldn't understand, Can you please repeat.")
        return ""
    return str(query).lower()

def listenImageGenerationPrompt():
    say("what image do you want to generate.")
    r = sr.Recognizer()
    while True:
        with sr.Microphone(device_index=2) as source:
            print("Listining...")
            r.pause_threshold = 1
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1)
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(query)
            # else:
            #     say(choice(random_reply))
        except Exception as e:
            say(f"Sorry sir, I Couldn't understand, Can you please repeat.")
            # print(f"Sorry sir, I Couldn't understand, Can you please repeat.")
            return ""
        return str(query).lower()

def imgPromptListening():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listining...")
        r.pause_threshold = 1
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1)
        audio = r.listen(source)
    try:
        say(randomReply())
        query = r.recognize_google(audio, language="en-in")
    except Exception as e:
        return ""
    return str(query).lower()

# def listenMail():
#     say("please enter the email address on the terminal whome you want to send the email to.")
#     reciver = input("Enter the email: ")
#     def subjectfun():
#         say("What will be the subject?")
#         r = sr.Recognizer()
#         with sr.Microphone(device_index=2) as source:
#             print("Listining...")
#             r.pause_threshold = 1
#             r.energy_threshold = 10000
#             r.adjust_for_ambient_noise(source, 1)
#             audio = r.listen(source)
#         try:
#             subject = r.recognize_google(audio, language="en-in")
#             if "leave it blank" in subject:
#                 return ""
#             else:
#                 return subject
#         except Exception as e:
#             say(f"Sorry sir, I Couldn't understand, Can you please repeat.")
#             subjectfun()
#     def messagefun():
#         say("What do you want to write in the mail sir?")
#         r = sr.Recognizer()
#         with sr.Microphone(device_index=2) as source:
#             print("Listining...")
#             r.pause_threshold = 1
#             r.energy_threshold = 10000
#             r.adjust_for_ambient_noise(source, 1)
#             audio = r.listen(source)
#         try:
#             message = r.recognize_google(audio, language="en-in")
#             return message
#         except Exception as e:
#             say(f"Sorry sir, I Couldn't understand, Can you please repeat.")
#             messagefun()
#     return [reciver, subjectfun(), messagefun()]

# def listenChat():
#     r = sr.Recognizer()
#     with sr.Microphone(device_index=2) as source:
#         # print("Listining...")
#         r.pause_threshold = 1
#         r.energy_threshold = 10000
#         r.adjust_for_ambient_noise(source, 1)
#         audio = r.listen(source)
#     try:
#         # print("Recognizing...")
#         query = r.recognize_google(audio, language="en-in")
#         # print(query)
#         # else:
#         #     say(choice(random_reply))
#     except Exception as e:
#         # say(f"Sorry sir, I Couldn't understand, Can you please repeat.")
#         # print(f"Sorry sir, I Couldn't understand, Can you please repeat.")
#         return "None"
#     return str(query).lower()
  
def wakeUpListen():
    r = sr.Recognizer()
    sr.Microphone.list_microphone_names()
    print("Listining...")
    with sr.Microphone(device_index=2) as source:
        r.pause_threshold = 1
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
    except Exception as e:
        return ""
    return str(query).lower()
  