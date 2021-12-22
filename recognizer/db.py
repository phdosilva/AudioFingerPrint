class Database():
    def __init__(self):
        self._value = {}

    def insert(self, audio_name, hashes):
        for H in hashes:
            h_code = H[0]
            h_delta = H[1]
            # insert into db
            if not h_code in self._value.keys():
                self._value[h_code] = {}

            self._value[h_code][h_delta] = audio_name

    def find(self, h_code):
        if not h_code in self._value.keys():
            return None
        
        return self._value[h_code]

    def debug(self):
        print(self._value)

    @property
    def value(self):
        return self._value