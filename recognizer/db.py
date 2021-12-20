class Database():
    def __init__(self):
        self._value = {}

    def insert(self, audio_name, hashes):
        if not audio_name in self._value.keys():
            self._value[audio_name] = []

        self._value[audio_name] += hashes

        return self._value

    @property
    def value(self):
        return self._value
