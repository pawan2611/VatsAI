from AppOpener import open, close
from speak import say

def openApp(app_name):
    say(f"Opening {app_name}")
    open(app_name, match_closest=True)

def closeApp(app_name):
    say(f"Closing {app_name}")
    close(app_name, match_closest=True, output=False)
