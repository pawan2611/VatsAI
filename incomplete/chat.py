from searchWeb import searchWebChat
from speak import say
from dotenv import load_dotenv
from listen import listenChat
load_dotenv()

def chat():
    print("Started Chatting...")
    chatStr = ""
    while True:
        query = listenChat()
        if "bye" in query:
            print(f"Pawan: {query}\nVats: Bye Sir")
            say("Bye Sir")
            break
        searchWebChat(query)
        print(f"Pawan: {query}\nVats:", end=" ")
        chatStr += f"Pawan: {query}\nVats: "
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chat bot, which likes to chat like a friend and can remember everything."},
            {"role": "user", "content": chatStr}
        ]
        )
        chatStr += f"{str(completion.choices[0].message.content)}\n"
        print(completion.choices[0].message.content)
        say(completion.choices[0].message.content)
    
# chat()
# chatStr = ""
# def chat():
#     while True:
#         query = listenChat()
#         if "bye" in query:
#             say("Bye Sir")
#             break
#         global chatStr
#         client = OpenAI()
#         chatStr += f"Pawan: {query}\nVats: "
#         print(f"Pawan: {query}\nVats:", end=" ")
#         completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a chat bot, which likes to chat like a friend."},
#             {"role": "user", "content": chatStr}
#         ]
#         )
#         chatStr += "str(completion.choices[0].message.content)\n"
#         print(completion.choices[0].message.content)
#         say(completion.choices[0].message.content)
    
# chat()