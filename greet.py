from datetime import datetime as dt
from decouple import config
from speak import say

USER = config("USER")
AI = config("AI")
dateTime = dt.now()

def greet():
    if(4 <= dateTime.hour < 12):
        say(f"Hello & Good Morning {USER} Sir! This is {AI} A.I. waiting for your orders.")
    elif(12 <= dateTime.hour < 17):
        say(f"Hello & Good Afternoon {USER} Sir! This is {AI} A.I. waiting for your orders.")
    elif(17 <= dateTime.hour < 24):
        say(f"Hello & Good Evening {USER} Sir! This is {AI} A.I. waiting for your orders.")
    elif(00 <= dateTime.hour < 4):
        say(f"Hello {USER} Sir! This is {AI} A.I. waiting for your orders.")