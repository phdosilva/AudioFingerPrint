from recognizer.decoder import extract_hashes

def register_matches(match_freq, titles, h_time):
  for title in titles.items():
    audio_time = title[0]
    audio_name = title[1]

    t_delta = audio_time - h_time

    if not t_delta in match_freq.keys():
      match_freq[t_delta] = {
        "audio_name": audio_name,
        "count": 0
      }

    match_freq[t_delta]["count"] += 1

def matching(database, hashes):

  title = "Unknown"

  matched_titles_freq = {}

  hit = 0
  miss = 0

  for Hash in hashes:
    h_code = Hash[0]
    h_time = Hash[1]

    titles = database.find(h_code)

    if titles == None:
      miss += 1
    else:
      hit += 1
      register_matches(matched_titles_freq, titles, h_time)

  print(f"hits = {hit}, miss = {miss}")

  max_freq = 0

  for matched_title in matched_titles_freq.values():
    if matched_title["count"] > max_freq:
      max_freq = matched_title["count"]
      title = matched_title["audio_name"]

  return title



    

