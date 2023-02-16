'''
Translator using IBM Watson API
'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = "2023-02-16"

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{VERSION}',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    '''
    Translate english text to french
    '''
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()

    french_text = translation["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    '''
    Translate french text to english
    '''
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()

    english_text = translation["translations"][0]["translation"]
    return english_text
