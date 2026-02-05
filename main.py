import os
import yt_dlp
import pygame
import sys
import time

def play_song(query):
    # Cleanup old file if exists
    if os.path.exists("song.mp3"):
        os.remove("song.mp3")

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'song.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }

    print(f"🔍 Searching for: {query}...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{query}"])
        
        pygame.mixer.init()
        pygame.mixer.music.load("song.mp3")
        pygame.mixer.music.play()
        
        print(f"🎶 Now Playing: {query}")
        print("Press Ctrl+C to stop playback.")
        
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\nPlayback stopped by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "humsafar"
    play_song(search_query)