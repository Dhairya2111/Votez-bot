import os
import yt_dlp
import pygame
import sys

def play_song(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'song.%(ext)s',
        'quiet': True
    }

    print(f"🔍 Searching for: {query}...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch1:{query}"])

    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play()
    
    print("🎶 Playing... Press Ctrl+C to stop.")
    try:
        while pygame.mixer.music.get_busy():
            continue
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\nStopped.")

if __name__ == "__main__":
    search_query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "husn"
    play_song(search_query)