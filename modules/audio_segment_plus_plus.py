from pydub import AudioSegment


class AudioSegmentPlusPlus(AudioSegment):
    @property
    def tracks(self):
        track_width: int = 371
        track_window: int = 16
        audio_tracks = []

        i: int = 0
        while i < len(self):
            audio_tracks.append(self[i: i + track_width])
            i += track_window

        return audio_tracks

    def export_audio_tracks(self, base_name='', dir='', format="mp3"):
        for (i, track) in enumerate(self.tracks):
            print(i)
            track.export(dir + base_name + f'{i}', format=format)

        return
