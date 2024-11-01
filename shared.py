import time

from pytube import YouTube, Playlist, Channel

VIDEO_SAVE_DIRECTORY = "./video"
AUDIO_SAVE_DIRECTORY = "./audio"

# def retry(func):
#     def wrapper(*args, **kwargs):
#         while True:
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 print(f"Function failed with exception: {e}. Retrying in 0.5 seconds...")
#                 time.sleep(0.5)
#     return wrapper

def retry(func):
    def wrapper(*args, **kwargs):
        success = False 
        while not success: 
            try:
                urls = func(*args, **kwargs)
                success = True
            except:
                print('Failed. Retrying...')
                time.sleep(0.5)
                continue
        return urls
    return wrapper

@retry
def download_video(url, filename, high_resolution=True):
    video = YouTube(url)
    print(url)
    print(filename)
    video = video.streams.get_highest_resolution() if high_resolution else video.streams.get_lowest_resolution()
    video.download(VIDEO_SAVE_DIRECTORY, filename=filename)
    print(f"{url} was downloaded successfully")

@retry
def get_title(video):
    return video.title

@retry
def get_playlist(url, include_titles=True):
    playlist = Playlist(url)
    print(type(playlist))
    # playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    urls = [url for url in playlist.video_urls]
    print(urls)
    if include_titles:
        titles = [get_title(video) for video in playlist.videos]
        return zip(urls, titles)
    return urls

@retry
def get_channel(url, include_titles=True):
    c = Channel(url)
    print(c.video_urls)
    urls = [url for url in c.video_urls]
    print(urls)
    if include_titles:
        titles = [get_title(video) for video in c.videos]
        return zip(urls, titles)
    return urls

@retry
def get_channel_url(video_url):
    return YouTube(video_url).channel_url + '/videos'

@retry
def download_audio(url, filename):
    video = YouTube(url)
    print('1')
    audio = video.streams.filter(only_audio = True).first()
    print('2')
    audio.download(AUDIO_SAVE_DIRECTORY, filename=filename)
    print(f"{url} was downloaded successfully")
