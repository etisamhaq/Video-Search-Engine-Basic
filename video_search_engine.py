from youtube_transcript_api import YouTubeTranscriptApi as yta
import re

def print_time(search_word, times):
    print(f"'{search_word}' was mentioned at:")
    for t in times:
        hours = int(t // 3600)
        minutes = int((t % 3600) // 60)
        seconds = int(t % 60)
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

video_id = "1aA1WGON49E"
transcript = yta.get_transcript(video_id, languages=['en'])
data = [t['text'] for t in transcript]
data = [re.sub(r"[^a-zA-Z0-9 ]", "", line) for line in data]
search_word = "Internet"

times = []
for i, line in enumerate(data):
    if search_word.lower() in line.lower():
        start_time = transcript[i]['start']
        times.append(start_time)

print_time(search_word, times)
