import pyttsx3
import speech_recognition as sr
from googletrans import Translator
from speak import say

# Initialize the Translator
translator = Translator()

# Dictionary of language names and their codes
language_dict = {
    "afrikaans": "af",
    "arabic": "ar",
    "bengali": "bn",
    "chinese (simplified)": "zh-CN",
    "chinese (traditional)": "zh-TW",
    "czech": "cs",
    "danish": "da",
    "dutch": "nl",
    "english": "en",
    "french": "fr",
    "german": "de",
    "greek": "el",
    "gujarati": "gu",
    "hindi": "hi",
    "italian": "it",
    "japanese": "ja",
    "kannada": "kn",
    "korean": "ko",
    "malayalam": "ml",
    "marathi": "mr",
    "portuguese": "pt",
    "punjabi": "pa",
    "russian": "ru",
    "spanish": "es",
    "swedish": "sv",
    "tamil": "ta",
    "telugu": "te",
    "turkish": "tr",
    "urdu": "ur",
    "vietnamese": "vi",
}

def listenTranslate(language="en-in"):
    """
    Listens to audio from the microphone and recognizes speech in the specified language.
    :param language: The language for speech recognition (default is English-India: "en-in").
    :return: The recognized text as a string, or an empty string if recognition fails.
    """
    r = sr.Recognizer()
    say("What do you want to translate?")
    attempts = 3  # Retry attempts for recognizing speech
    while attempts > 0:
        with sr.Microphone(device_index=2) as source:
            r.pause_threshold = 1
            r.energy_threshold = 300  # Lower threshold for ambient noise
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = r.listen(source)
        try:
            print("Recognizing...")
            queryText = r.recognize_google(audio, language=language)
            print("You said:", queryText)
            break
        except sr.UnknownValueError:
            attempts -= 1
            say(f"Sorry, I didn't catch that. Please repeat.")
        except Exception as e:
            print(f"Error: {e}")
            attempts -= 1
    else:
        say("Sorry, I couldn't understand. Exiting.")
        return None

    say("To which language do you want to translate?")
    attempts = 3  # Retry attempts for language recognition
    while attempts > 0:
        with sr.Microphone(device_index=2) as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening for language...")
            audio = r.listen(source)
        try:
            print("Recognizing language...")
            queryLanguage = r.recognize_google(audio, language=language)
            queryLanguage = queryLanguage.strip().lower()
            print(queryLanguage)
            if queryLanguage in language_dict:
                return [language_dict[queryLanguage], queryText]
            else:
                say(f"Sorry, I don't support {queryLanguage}. Try another language.")
        except sr.UnknownValueError:
            attempts -= 1
            say(f"Sorry, I didn't catch that. Please repeat.")
        except Exception as e:
            print(f"Error: {e}")
            attempts -= 1
    else:
        say("Sorry, I couldn't understand the language. Exiting.")
        return None

def translate_to_any_language(text, target_language):
    """
    Translates text to a specified target language.
    :param text: Text to be translated.
    :param target_language: The language code for translation (e.g., 'hi' for Hindi).
    :return: Translated text.
    """
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"An error occurred: {e}"


# if __name__ == "__main__":
#     query = "translate"
#     if "translate" in query:
#         result = listenTranslate()
#         if result:
#             langCode, text = result
#             translatedText = translate_to_any_language(text, langCode)
#             print("Translated Text:", translatedText)
#             say(f"The translation is: {translatedText}")
