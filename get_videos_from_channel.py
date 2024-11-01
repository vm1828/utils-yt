import youtube_dl
import csv

# Replace with the channel URL you want to fetch videos from
CHANNEL_URL = 'https://www.youtube.com/channel/UCtYLUTtgS3k1Fg4y5tAhLbw/videos'

def get_video_links(channel_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel_url, download=False)
        
    video_links = []
    
    if 'entries' in result:
        for entry in result['entries']:
            video_title = entry.get('title')
            video_url = entry.get('url')
            if video_title and video_url:
                video_links.append({'title': video_title, 'url': f'https://www.youtube.com/watch?v={video_url}'})
    
    return video_links

def save_to_csv(video_links, filename='video_links.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'url'])
        writer.writeheader()
        for video in video_links[::-1]:
            writer.writerow(video)

def main():
    video_links = get_video_links(CHANNEL_URL)
    save_to_csv(video_links)
    # Print the video links
    for video in video_links:
        print(f"{video['title']}: {video['url']}")

if __name__ == "__main__":
    main()
