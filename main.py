from ai import AI
from Features.Wishme import wishme
from Features.Play_song import play_songs
from Features.Dtime import date, day, time
from Features.Default import ip, netspeed

alf = AI()

# alf.name = "Robbie the Robot"

wishme()
query = ""
while True:
    query = alf.listen()
    if "čas" in query:  # Čas
        time()
    elif "datum" in query:
        date()
    elif "den" in query:
        day()
    elif "Přehraj hudbu" in query:
        play_songs()
    elif "ip adresa" in query:
        ip()
    elif "rychlost připojení" in query:
        netspeed()
    elif "konec" in query:
        quit()

    # do commands
