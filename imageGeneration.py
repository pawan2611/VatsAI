import requests, os
from datetime import datetime as dt
from listen import listenImageGenerationPrompt
from speak import say

def download_image(prompt, width=768, height=768, model='flux', seed=None):
    url = f"https://image.pollinations.ai/prompt/{prompt}?width={width}&height={height}&model={model}&seed={seed}"
    response = requests.get(url)
    cwd = os.getcwd()
    if not os.path.exists("Image"):
        os.mkdir("Image")
    name = ''.join(n for n in str(dt.now()) if n.isalnum())
    path = os.path.join(cwd+f"\\Response\\generatedImage{name}.jpg")
    with open(path, 'wb') as file:
        file.write(response.content)
    print('Image downloaded!')
    say("Image saved inresponse folder")

# download_image(listenImageGenerationPrompt(), width=1280, height=720, model='flux', seed=42)