from recognizer.audio_segment_plus_plus import AudioSegmentPlusPlus as AudioSegment

# song = AudioSegment.from_mp3("mp3/<song name>.mp3")
# samplings = song.samplings

from recognizer.database import Database


db = Database()
db.setup()

