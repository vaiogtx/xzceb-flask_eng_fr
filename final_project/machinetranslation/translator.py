"""
The final project for the course
"""
# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]
VERSION = "2018-05-01"
authenticator = IAMAuthenticator(apikey=apikey)


def get_models():
    """
    Get the list of available models
    :return:
    """
    translator = LanguageTranslatorV3(version=VERSION,
                                      authenticator=authenticator)
    translator.set_service_url(url)
    models = translator.list_identifiable_languages().get_result()
    print(models)


def english_to_french(english_text):
    """
    Translates the input English text into French
    :param english_text:
    :return:
    """
    translator = LanguageTranslatorV3(version=VERSION,
                                      authenticator=authenticator)
    translator.set_service_url(url)
    translation = translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text = translation["translations"][0]["translation"]

    return french_text


def french_to_english(french_text):
    """
    Translates the input French text into English
    :param french_text:
    :return:
    """
    translator = LanguageTranslatorV3(version=VERSION,
                                      authenticator=authenticator)
    translator.set_service_url(url)
    translation = translator.translate(text=french_text, model_id="fr-en").get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text


if __name__ == "__main__":
    english_to_french("Hello World")
