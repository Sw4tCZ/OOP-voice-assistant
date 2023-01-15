from body.Speak import *
from requests import get
import speedtest
from colorama import Fore, init

init(autoreset=True)
def ip():
    ip = get('https://api.ipify.org').text
    print(f"Ip adresa je {ip}")
    speak(f"Ip adresa je {ip}")

def netspeed():
    speak("Zjišťuji rychlost připojení. Tato operace zabere nějakou chvilku.")
    st = speedtest.Speedtest()
    st.get_best_server()
    st.download()
    st.upload()
    res_dict = st.results.dict()
    dwnl = str(res_dict['download'])[:2] + "." + \
           str(res_dict['download'])[2:4]
    upl = str(res_dict['upload'])[:2] + "." + str(res_dict['upload'])[2:4]
    print(Fore.MAGENTA + "=" * 80)
    print(Fore.YELLOW +
          f"Download: {dwnl}mbps({float(dwnl) * 0.125:.2f}MBs) | Upload:{upl}mbps ({float(upl) * 0.125:.2f}MBs) | Ping: {res_dict['ping']:.2f}ms".center(
              80))
    print(Fore.MAGENTA + "=" * 80)
    speak(f"Rychlost stahování je:{dwnl} a rychlost nahrávání je:{upl}")

