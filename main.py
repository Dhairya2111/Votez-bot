import json
import os

QUEUE_FILE = "queue.json"

def get_queue():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, "r") as f:
        return json.load(f)

def save_queue(queue):
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f)

def add_to_queue(song_name):
    queue = get_queue()
    queue.append(song_name)
    save_queue(queue)
    print(f"✅ Added to queue: {song_name}")

def show_queue():
    queue = get_queue()
    if not queue:
        print("Empty queue.")
    else:
        print("\n--- Current Queue ---")
        for i, song in enumerate(queue, 1):
            print(f"{i}. {song}")