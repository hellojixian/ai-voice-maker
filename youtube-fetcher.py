import sys
import pytube
from moviepy.editor import *

# read the content id from the command line arguments
if len(sys.argv) < 2:
    print("Please provide a YouTube video content id")
    print("Example: https://www.youtube.com/watch?v=CONTENT_ID")
    print("Usage: python youtube-fetcher.py CONTENT_ID [START_OFFSET] [END_OFFSET]")
    sys.exit(1)
content_id = sys.argv[1]
start_offset = (int)(sys.argv[2]) if len(sys.argv)==3 else 0
end_offset = (int)(sys.argv[3]) if len(sys.argv)==4 else 0

# Set the YouTube video URL
video_url = f"https://www.youtube.com/watch?v={content_id}"

# Create a YouTube object
youtube = pytube.YouTube(video_url)

# Get the audio stream
audio_stream = youtube.streams.filter(only_audio=True).get_audio_only()

# Download the audio stream
audio_filename = audio_stream.download()
# Convert the audio file to WAV format
audio_clip = AudioFileClip(audio_filename)
trimmed_audio_clip = audio_clip.subclip(start_offset, audio_clip.duration - end_offset)

trimmed_audio_clip.write_audiofile(f"output/{content_id}.wav", codec="pcm_s16le")

# Delete the original audio file
audio_clip.close()
os.remove(audio_filename)

print("Audio extraction complete!")