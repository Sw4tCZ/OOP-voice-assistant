import os
import random


def play_songs():
        music_dir = "C:/Users/tomkr/Desktop/music" # Složka nesmí být systémová hudba.
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        for song in songs:
                if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, rd))

