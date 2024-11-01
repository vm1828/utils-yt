from pytube import YouTube
import csv
import os
from shared import *

# CSV file containing video links and titles
CSV_FILE = 'video_links.csv'

def read_video_links(csv_file):
    video_links = []
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            video_links.append(row)
    return video_links

def download_videos(video_links):
    # Create 'videos' folder if it doesn't exist
    os.makedirs('videos', exist_ok=True)
    
    for i, video in enumerate(video_links, start=0):
        try:
            video_title = video['title']
            video_url = video['url']

            # Create a YouTube object
            yt = YouTube(video_url)

            # Get the highest resolution stream
            stream = yt.streams.get_highest_resolution()

            # Download the video
            print(f"Downloading: {video_title}")
            filename_prefix = f"{i:03d}"  # Number prefix with leading zeros (e.g., 001, 002, etc.)
            filename = f"videos/{filename_prefix} - {video_title}.mp4"
            # download_video(video_url, filename)
            stream.download(filename=filename)
        except:
            os.remove(filename)
            with open('failures.txt', 'a') as f:
                f.write(f'{filename}\n')
            continue

def main():
    video_links = read_video_links(CSV_FILE)
    download_videos(video_links)

if __name__ == "__main__":
    main()
