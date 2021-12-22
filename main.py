import os

from recognizer.db import Database as FakeDatabase
from recognizer.decoder import extract_hashes
from recognizer.matching import matching
from pydub import AudioSegment

def generate_db():
    audio_name_list = os.listdir('mp3/')
    db = FakeDatabase()

    # creating a db
    for i in range(4):
        audio_path = f'mp3/{audio_name_list[i]}'
        print(f'Extracting fingerprints from {audio_path} like audio_{i}')

        hashes = extract_hashes(audio_path)
        db.insert(audio_name=f'{audio_name_list[i]}', hashes=hashes)

    return db

def test_audio(database):
    audio_name_list = os.listdir('test/')

    # get the first audio
    for i in range(1):
        audio_path = f'test/{audio_name_list[i]}'
        print(f'Extracting fingerprints from {audio_path} like audio_{i}')
        hashes = extract_hashes(audio_path)
        music_title = matching(database, hashes)

        output = "this music is: " + music_title
        print(output)

def main():

    db = generate_db()
    test_audio(db)

if __name__ == "__main__":
    main()