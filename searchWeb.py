import google.generativeai as genai, os
from datetime import datetime as dt
from decouple import config
from speak import say
# import openai
from replies import randomReply
from dotenv import load_dotenv
# from time import sleep
# from listen import listenBool
# from onlineFunctions import searchGoogle
load_dotenv()

GEMINI_API_KEY = config("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def searchWebChat(query):
    say(randomReply())
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content(query)
    responseText = response.resolve()
    shortAns = ""
    if response.prompt_feedback.block_reason:
        return ["Sorry Sir, I can't provide The Information"]
    for lit in responseText:
        if lit == ".":
            break
        shortAns=shortAns+lit
    print(shortAns)
    say(shortAns)

def searchWeb(query):
    say(randomReply())
    model = genai.GenerativeModel('gemini-pro')
    query = query.replace("on google","")
    # query = query.replace("what's","")
    # query = query.replace("tell me","")
    # query = query.replace("search for","")
    # query = query.replace("what is","")
    # query = query.replace("what do you mean by","")
    response = model.generate_content(query)
    responseText = ""
    shortAns = ""
    if response.prompt_feedback.block_reason:
        return ["Sorry Sir, I can't provide The Information"]
    for lit in response.text:
        if lit == "*":
            continue
        responseText=responseText+lit
    name = ''.join(n for n in str(dt.now()) if n.isalnum())
    if not os.path.exists("Response"):
        os.mkdir("Response")
    with open(f"./Response/response{name}.py","w") as file:
        file.write(responseText)
    os.rename(f"./Response/response{name}.py", f"./Response/response{name}.txt")
    say("Response saved in the Response folder.")
    for lit in responseText:
        if lit == ".":
            break
        shortAns=shortAns+lit
    print(shortAns)
    say(shortAns)
    # sleep(1)
    say("More Information on the Terminal.")
    # sleep(1)
    # say("should i open google tab?")
    # if "yes" in listenBool():
    #     searchGoogle(query)
    # else:
    #     say("Ok sir")
        
# def chatgpt(query):
#     say(randomReply())
#     openai.api_key = config("OPENAI_API_KEY")
#     client = openai.OpenAI()
#     completion = openai.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a programming assistant, skilled in making and explaining complex programs."},
#         {"role": "user", "content": query}
#     ]
#     )
#     data = completion.choices[0].message.content
#     name = ''.join(n for n in str(dt.now()) if n.isalnum())
#     if not os.path.exists("OpenaiResponses"):
#         os.mkdir("OpenaiResponses")
#     with open(f"./OpenaiResponses/response{name}.py","w") as file:
#         file.write(data)
#     os.rename(f"./OpenaiResponses/response{name}.py", f"./OpenaiResponses/response{name}.txt")
#     say("Response saved in the Open A I Responses folder.")

# query = "using artificial intelligence write a python program to draw star using turtle"
# chatgpt(query)

