import os
import numpy as np

from recognizer.fingerprint import fingerprint
from recognizer.audio_segment_plus_plus import AudioSegmentPlusPlus as AudioSegment

audio_name_list = os.listdir('mp3/')

def extract_channels(audio):
    channels = []

    # convert to manipulable data
    audio_data = np.frombuffer(audio.raw_data, np.int16)

    # get data by audio channels
    # channels are often 2, on stereo audio
    for channel_iterator in range(audio.channels):
        channels.append((audio_data[channel_iterator::audio.channels]))

    return channels


for i in range(1):
    print(f'{i}')

    audio_path = f'mp3/{audio_name_list[i]}'
    audio = AudioSegment.from_mp3(audio_path)

    channels = extract_channels(audio)

    channels_fingerprint_hashes = []
    for channel in channels:
        channels_fingerprint_hashes.append(fingerprint(channel))

    # print(len(channels_fingerprint_hashes))
    # print(channels_fingerprint_hashes[1])

    right_one = AudioSegment.from_mp3('right_one.mp3')
    channels_sample = extract_channels(audio.random_sampling)

    channels_sample_fingerprint_hashes = []
    for channel in channels_sample:
        channels_sample_fingerprint_hashes.append(fingerprint(channel))


    for channel in channels_sample_fingerprint_hashes:
        for hash in channel:
            for channel_2 in channels_fingerprint_hashes:
                for hash_2 in channel_2:
                    # print(hash[0], hash_2[0])

                    if hash[0] == hash_2[0]:
                        print("I found it!")


