#speech_recognition for speech to text and im also using GOOGLE API fr speech
#pyaudio is used in recoginser 
import speech_recognition as sp 
import pyttsx3
import pyaudio
# from googletrans import Translator

speech = sp.Recognizer()
# language = Translator()

def record():
    try:
        with sp.Microphone() as source:
            speech.adjust_for_ambient_noise(source,duration=0.2)
            audio = speech.listen(source,timeout=5, phrase_time_limit=5)
            text = speech.recognize_google(audio)
    #different language can be used if you have them in device downloaded
            return text
            
    except :
        print("ERROR OCCURED")

        return;

def output(text):
    #pyttsx is for text to speech
    print(text)
    if text == None:
        text = "ERROR OCCURED"
    
    # text1 = language.translate(text,dest="hi-IN")
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    # India = "Hindi"
    # engine.setProperty('voice',India)
    engine.say(text)
    engine.runAndWait()

    return;

text = record()
output(text)
