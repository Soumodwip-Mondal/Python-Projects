from moviepy import *

# Load the video file
video = VideoFileClip("Video.mp4")

# Extract the audio
audio = video.audio

# Save the audio to a file
audio.write_audiofile("audio.mp3")

print("Completed")