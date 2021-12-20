import numpy as np

from recognizer.fingerprint import fingerprint
from recognizer.audio_segment_plus_plus import AudioSegmentPlusPlus as AudioSegment


def extract_channels(audio):
    channels = []

    # convert to manipulable data
    audio_data = np.frombuffer(audio.raw_data, np.int16)

    # get data by audio channels
    # channels are often 2, on stereo audio
    for channel_iterator in range(audio.channels):
        channels.append((audio_data[channel_iterator::audio.channels]))

    return channels


def extract_hashes(audio_path):
    audio = AudioSegment.from_mp3(audio_path)

    channels = extract_channels(audio)

    channels_fingerprint_hashes = []
    for channel in channels:
        channels_fingerprint_hashes.append(fingerprint(channel))

    channels_sample = extract_channels(audio.random_sampling)

    hashes = []

    for channel in channels_sample:
        hashes += fingerprint(channel)

    return hashes
