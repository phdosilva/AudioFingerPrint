from recognizer.audio_segment_plus_plus import AudioSegmentPlusPlus as AudioSegment
import numpy as np
from hashlib import sha1
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


audio_path = "mp3/2 - -- MC GASPAR E MC REIZINHO Feat. MC VITTIN PV - BOTADÃO - REMIX BREGA FUNK(MP3_160K).mp3"

audio = AudioSegment.from_mp3(audio_path)

channels = [] # each one will have audio

audio_data = np.frombuffer(audio.raw_data, np.int16)

for channel_iterator in range(audio.channels): # number fo channels that audios have (usualy 2)
    channels.append((audio_data[channel_iterator::audio.channels]))

def unique_hash(file_path: str) -> str:
    """ Small function to generate a hash to uniquely generate
    a file. Inspired by MD5 version here:
    http://stackoverflow.com/a/1131255/712997

    Works with large files.

    :param file_path: path to file.
    :param block_size: read block size.
    :return: a hash in an hexagesimal string form.
    """
    s = sha1()
    with open(file_path, "rb") as f:
        while True:
            buf = f.read()
            if not buf:
                break
            s.update(buf)
    return s.hexdigest().upper()

arr = plt.specgram(
        channels[0],
        NFFT=371,
        noverlap=16
)

print(arr)


plt.specgram(
        channels[1],
        NFFT=371,
        noverlap=16
)


print(arr2D)

print(unique_hash(audio_path))

for channel in channels:
    print(len(channel))