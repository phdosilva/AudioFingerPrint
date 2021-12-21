import os

from recognizer.db import Database as FakeDatabase
from recognizer.decoder import extract_hashes

audio_name_list = os.listdir('mp3/')
db = FakeDatabase()

# creating a fake db
for i in range(10):
    audio_path = f'mp3/{audio_name_list[i]}'
    print(f'Extracting fingerprints from {audio_path} like audio_{i}')

    hashes = extract_hashes(audio_path)
    db.insert(audio_name=f'audio_{i}', hashes=hashes)

# printing fake db
for audio in db.value:
    print(audio)
