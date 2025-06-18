import requests, wikipedia, smtplib, json, time, pywhatkit as kit, os
from speak import say
from datetime import datetime as dt
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
# from listen import listenMail
# from decouple import config


def weather(city):
    jsonDataStr = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=93d5251fba6408650b207b2f9a54061c#").text
    # data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=93d5251fba6408650b207b2f9a54061c#")
    data = json.loads(jsonDataStr)
    responseText = f"Currently there's {data['weather'][0]['main']} kind of weather in {city} the temperature is {round(data['main']['temp']-273,1)} degree centigrates ,the max and min of tody is {round(data['main']['temp_max']-273,1)} degrees and {round(data['main']['temp_min']-273,1)} degrees respectively and the wind speed is {data['wind']['speed']} kilometers per hour."
    print(f"Currently there's {data['weather'][0]['main']} kind of weather in {city} the temperature is "+
        f"{round(data['main']['temp']-273,1)} degree centigrates ,the max and min of tody is {round(data['main']['temp_max']-273,1)} "+
        f"degrees and {round(data['main']['temp_min']-273),1} degrees respectively and the wind speed is "+
        f"{data['wind']['speed']} kilometers per hour.")
    say(f"Currently there's {data['weather'][0]['main']} kind of weather in {city} the temperature is "+
        f"{round(data['main']['temp']-273,1)} degree centigrates ,the max and min of tody is {round(data['main']['temp_max']-273,1)} "+
        f"degrees and {round(data['main']['temp_min']-273),1} degrees respectively and the wind speed is "+
        f"{data['wind']['speed']} kilometers per hour.")
    name = ''.join(n for n in str(dt.now()) if n.isalnum())
    name = ''.join(n for n in str(dt.now()) if n.isalnum())
    if not os.path.exists("Response"):
        os.mkdir("Response")
    with open(f"./Response/response{name}.py","w") as file:
        file.write(responseText)
    os.rename(f"./Response/response{name}.py", f"./Response/response{name}.txt")
    say("Response saved in the Response folder.")
    
def news():
    url = "https://api.worldnewsapi.com/search-news?language=en&source-country=in&api-key=b2f33f3f57f64cb19026cf632ea34fa0"
    response = requests.get(url)
    try:
        if response.status_code == 200:
            resJson = json.dumps(response.json(), indent=4)
            resJson = json.loads(resJson)['news']
            # name = ''.join(n for n in str(dt.now()) if n.isalnum())
            # if not os.path.exists("Response"):
            #     os.mkdir("Response")
        # strNews = ""
        # for i in resJson:
        #     strNews = strNews+i["title"]+"\n"+i["url"]+"\n"
        #     with open(f"./Response/response{name}.txt","a") as file:
        #         file.write(strNews)
        # say("Response saved in the Response folder.")
        for i in resJson:
            print(i["title"])
            print(i["url"]+"\n")
            say(i["title"])
            time.sleep(0.5)
    except Exception as e:
        print(e)
        say("There's some issue getting the news")
    # print(response)

def findIP():
    ipv4 = json.loads(requests.get('https://api.ipify.org?format=json').text)
    say(f"Your IP address is {ipv4['ip']}")
    return ipv4['ip']
    
def findIPLocation():
    say("Please enter the ip in the terminal.")
    # ip = json.loads(requests.get('https://api.ipify.org?format=json').text)
    ip = input("Enter the IP: ")
    jsonStr = json.loads(requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=9e48c91b397447c5a405e4e665c02ef6&ip={ip}').text)
    say(f"The IP address is in {jsonStr['city']} city of {jsonStr['country_name']}")
    print(f"Latitude: {jsonStr['latitude']}\nLongitude: {jsonStr['longitude']}")
    say("Please check the terminal for the Latitudes and Longitudes.")
# findIPLocation()
def findMyLocation():
    ip = findIP()
    jsonStr = json.loads(requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=9e48c91b397447c5a405e4e665c02ef6&ip={ip}').text)
    say(f"Your Location is in {jsonStr['city']} city of {jsonStr['country_name']}")
    print(f"Latitude: {jsonStr['latitude']}\nLongitude: {jsonStr['longitude']}")
    say("Please check the terminal for the Latitudes and Longitudes.")
    
def searchWiki(query):
    say("Opening Wikipedia")
    query = query.replace("search for","")
    query = query.replace("on wikipedia","")
    result = wikipedia.summary(query, sentence = 2)
    name = ''.join(n for n in str(dt.now()) if n.isalnum())
    if not os.path.exists("Response"):
        os.mkdir("Response")
    with open(f"./Response/response{name}.py","w") as file:
        file.write(result)
    os.rename(f"./Response/response{name}.py", f"./Response/response{name}.txt")
    say("Response saved in the Response folder.")
    print(result)
    say("and displayed on the terminal")

def searchGoogle(query):
    say("Opening Google")
    query = query.replace("search for","")
    query = query.replace("on google","")
    query = query.replace("using artificial intelligence ","")
    kit.search(query)
    
def playYoutube(query):
    say("Opening youtube")
    query = query.replace("play","")
    query = query.replace("on youtube","")
    kit.playonyt(query)
    
# def sendMail():
#     mailData  = listenMail()
#     reciver = mailData[0]
#     subject = mailData[1]
#     message = mailData[2]
    
#     try:
#         email = MIMEMultipart()
#         email['From'] = EMAIL
#         email['To'] = reciver
#         email['Subject'] = subject
#         email.attach(MIMEText(message, "plain"))
#         with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
#             server.starttls()
#             server.login(EMAIL, PASSWORD)
#             server.sendmail(EMAIL, reciver, email.as_string())
#         say("Your Email has been Sent")
#         return True
#     except Exception as e:
#         print(e)
#         say(f"Your email cann't sent due to {e}.")
#         return False
        