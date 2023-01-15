from body.Speak import *
import datetime

def time():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(time)
    print(time)


def day():
    now = datetime.datetime.now()
    dny_v_tydnu = {0: "pondělí", 1: "úterý", 2: "středa", 3: "čtvrtek", 4: "pátek", 5: "sobota", 6: "neděle"}

    den = dny_v_tydnu[now.weekday()]
    speak("Dnes je: {}".format(den))


def date():
    date = int(datetime.datetime.now().day)
    now = (datetime.datetime.now())
    from month import months
    month = (months[now.month])
    year = int(datetime.datetime.now().year)
    print(f"Den: {date}., Měsíc: {month}, Rok: {year}")
    speak(f"Den: {date}., Měsíc: {month}, Rok: {year}")