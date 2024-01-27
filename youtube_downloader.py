#!/usr/bin/env python3

# Import the pytube library for YouTube video manipulation
import pytube

# Prompt the user to input the video URL
video_url = input("Write your video url: ")

# Create a YouTube object with the provided video URL
yt = pytube.YouTube(video_url)

# Get the stream with the highest resolution 
stream = yt.streams.get_highest_resolution()

# Inform the user that the video is being downloaded
print("Video is being downloaded!")

# Download the video using the selected steam
stream.download()
