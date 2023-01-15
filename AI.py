import pyttsx3
import speech_recognition as sr

class AI():
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        cs_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_csCZ_Jakub"
        self.engine.setProperty('voice', cs_voice_id)
        voicespeed = 180
        self.engine.setProperty('rate', voicespeed)
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

    def speak(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    def listen(self):
        print("Poslouchám")
        with self.m as source:
            audio = self.r.listen(source)
        print("Mám to.")
        try:
            query = self.r.recognize_google(audio, show_all=False, language="cs-CZ")
            sententce = "Řekl jsi" + query
            self.engine.say(sententce)
            self.engine.runAndWait()
        except:
            print("Omlouvám se, nestihl jsem to.")
            self.engine.say("Omlouvám se, nestihl jsem to.")
            self.engine.runAndWait()
            return ""
        query = str(query).lower()
        return query
