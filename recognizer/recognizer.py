import os
import numpy as np

from recognizer.fingerprint import fingerprint
from recognizer.audio_segment_plus_plus import AudioSegmentPlusPlus as AudioSegment

def get_matches(channel_sample):
    hashes = fingerprint.fingerprint(channel_sample)

    mapper = {}
    for hash, offset in hashes:
        mapper[hash.uper()] = offset
    values = mapper.keys()

    pass


def return_matches(self, hashes: List[Tuple[str, int]],
                   batch_size: int = 1000) -> Tuple[List[Tuple[int, int]], Dict[int, int]]:
    """
    Searches the database for pairs of (hash, offset) values.

    :param hashes: A sequence of tuples in the format (hash, offset)
        - hash: Part of a sha1 hash, in hexadecimal format
        - offset: Offset this hash was created from/at.
    :param batch_size: number of query's batches.
    :return: a list of (sid, offset_difference) tuples and a
    dictionary with the amount of hashes matched (not considering
    duplicated hashes) in each song.
        - song id: Song identifier
        - offset_difference: (database_offset - sampled_offset)
    """
    # Create a dictionary of hash => offset pairs for later lookups
    mapper = {}
    for hsh, offset in hashes:
        if hsh.upper() in mapper.keys():
            mapper[hsh.upper()].append(offset)
        else:
            mapper[hsh.upper()] = [offset]

    values = list(mapper.keys())

    # in order to count each hash only once per db offset we use the dic below
    dedup_hashes = {}

    results = []
    with self.cursor() as cur:
        for index in range(0, len(values), batch_size):
            # Create our IN part of the query
            query = self.SELECT_MULTIPLE % ', '.join([self.IN_MATCH] * len(values[index: index + batch_size]))

            cur.execute(query, values[index: index + batch_size])

            for hsh, sid, offset in cur:
                if sid not in dedup_hashes.keys():
                    dedup_hashes[sid] = 1
                else:
                    dedup_hashes[sid] += 1
                #  we now evaluate all offset for each  hash matched
                for song_sampled_offset in mapper[hsh]:
                    results.append((sid, offset - song_sampled_offset))

        return results, dedup_hashes

def _recognize(self, *data):
    fingerprint_times = []
    hashes = set()  # to remove possible duplicated fingerprints we built a set.
    for channel in data:
        fingerprints, fingerprint_time = self.dejavu.generate_fingerprints(channel, Fs=self.Fs)
        fingerprint_times.append(fingerprint_time)
        hashes |= set(fingerprints)




    mapper = {}
    for hash, offset


    return return_matches (fingerprint.fingerprint(channel_sample, Fs=Fs))

def recognize(audio):

