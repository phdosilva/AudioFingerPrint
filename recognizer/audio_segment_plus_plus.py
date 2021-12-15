from pydub import AudioSegment

from recognizer.settings import (DEFAULT_SAMPLING_OFFSET,
                                 DEFAULT_SAMPLING_WIDTH)


class AudioSegmentPlusPlus(AudioSegment):
    @property
    def samplings(self):
        sampling_width: int = DEFAULT_SAMPLING_WIDTH
        offset: int = DEFAULT_SAMPLING_OFFSET
        audio_samplings = []

        i: int = 0
        while i < len(self):
            audio_samplings.append(self[i: i + sampling_width])
            i += offset

        return audio_samplings

    def export_audio_tracks(self, base_name='', dir='', format="mp3"):
        for (i, track) in enumerate(self.samplings):
            print(i)
            track.export(dir + base_name + f'{i}', format=format)

        return
