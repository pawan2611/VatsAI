import google.generativeai as genai, PIL.Image, cv2, os
from datetime import datetime as dt
from speak import say
from listen import imgPromptListening
from decouple import config

GOOGLE_API_KEY = config("GEMINI_API_KEY")
os.environ['GOOGLE_API_KEY']=GOOGLE_API_KEY
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def imageCapture():
    # Open webcam
    cap = cv2.VideoCapture(0)
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        say("Sorry sir there's some error with the webcam")
        print("Sorry sir there's some error with the webcam")
        return None
    # Read and display frame
    say("Capturing Image in 4 seconds.")
    start_time = cv2.getTickCount()  # Get current tick count
    while True:
        ret, frame = cap.read()
        cv2.imshow("Webcam", frame)
        current_time = cv2.getTickCount()  # Get current tick count
        elapsed_time = (current_time - start_time) / cv2.getTickFrequency()  # Calculate elapsed time in seconds
        if elapsed_time >= 4:  # Capture image after 4 seconds
            break
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Quit if 'q' is pressed
            cap.release()
            cv2.destroyAllWindows()
            say("Capture cancelled.")
            return None
    # Generate path for saving image
    cwd = os.getcwd()
    if not os.path.exists("Image"):
        os.mkdir("Image")
    name = ''.join(n for n in str(dt.now()) if n.isalnum())
    path = os.path.join(cwd+f"\\Image\\capturedImage{name}.jpg")
    path2 = os.path.join(cwd+f"\\Image\\capturedImage{name}.jpg")
    # Save captured image
    cv2.imwrite(path, frame)
    # Release webcam and close window
    cap.release()
    cv2.destroyAllWindows()
    return path2

def imgDetails(imgPath):
    if imgPath == None:
        say("No Image Found")
        return
    try:
        img = PIL.Image.open(imgPath)
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        say("What do you want to know about this image sir.")
        query = imgPromptListening()
        # if query == "":
        #     prompt = "Explain what is in the picture or if the picture contains any person tell who is he or she. In atleast 20 words."
        # else:
        #     prompt = query
        prompt = "Explain what is in the picture or if the picture contains any person tell who is he or she or if it contains any object tell about it. In atleast 20 words."
        response = model.generate_content([prompt, img], stream=True)
        response.resolve()
        # data=str(response)
        # # data = str(re.sub(r'\W+',' ',data))
        # data = str(re.sub(r'[^\w\s.,]',' ',data))
        # start_literal = "result glm.GenerateContentResponse   candidates      content     parts      text     "
        # end_literal = "   ,  role    model  ,  finish_reason   1,  index   0,  safety_ratings      category   9,  probability   1,  blocked   False ,   category"
        # start_index = re.search(start_literal, data).end()
        # end_index = re.search(end_literal, data).start()
        # data = data[start_index:end_index]
        print(response.text)
        say(response.text)
        return
    except Exception as e:
        say("Sorry sir I couldn't find anything about the image.")
        print(e)
        return
    