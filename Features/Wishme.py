from body.Speak import *
import datetime

def wishme():
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 9:
        speak("Dobré ráno")
    elif hour >= 9 and hour <= 11:
        speak("Dobré dopoledne")
    elif hour == 12:
        speak("Dobré poledne")
    elif hour >= 12 and hour <= 17:
        speak("Dobré odpoledne")
    elif hour >= 17 and hour <= 23:
        speak("Dobrý večer")
    else:
        speak("Dobrou noc")

    speak("Jak vám mohu pomoci?")
