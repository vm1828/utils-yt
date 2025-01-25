import time

import os
import subprocess
from pytubefix import YouTube, Playlist, Channel
from pytubefix.cli import on_progress

VIDEO_DIR = "./video"
AUDIO_DIR = "./audio"

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
            except Exception as e:
                print(f'Failed: {e}. \nRetrying...')
                time.sleep(1)
                continue
        return urls
    return wrapper

# @retry
# def download_video(url, filename, high_resolution=True):
#     video = YouTube(url)
#     print(url)
#     print(filename)
#     video = video.streams.get_highest_resolution() if high_resolution else video.streams.get_lowest_resolution()
#     video.download(VIDEO_DIR, filename=filename)
#     print(f"{url} was downloaded successfully")


@retry
def download_video(url, filename):
    yt = YouTube(url, on_progress_callback=on_progress)
    print(url)
    print(filename)

    tmp_video_file = 'video.mp4'
    tmp_audio_file = 'audio.mp4'

    yt.streams.filter(
        adaptive=True, file_extension='mp4', only_video=True
    ).order_by('resolution').desc().first().download(filename=tmp_video_file)
    yt.streams.filter(
        adaptive=True, file_extension='mp4', only_audio=True
    ).order_by('abr').desc().first().download(filename=tmp_audio_file)

    output_file = os.path.join(VIDEO_DIR, filename.replace('/', '_or_'))
    cmd = f'ffmpeg -i {tmp_video_file} -i {tmp_audio_file} -c:v copy -c:a aac "{output_file}.mp4"'
    print(cmd)
    subprocess.call(cmd, shell=True)
    os.remove(tmp_video_file)
    os.remove(tmp_audio_file)

    # resolutions = ['1080p', '720p', '480p', '360p', '240p']
    # for res in resolutions:
    #     for stream in yt.streams:
    #         if stream.resolution==res:
    #             stream.download(VIDEO_DIR, filename=filename)
    #             return


@retry
def get_title(video):
    return video.title


@retry
def get_playlist(url, include_titles=True):
    playlist = Playlist(url)
    # playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    urls = [url for url in playlist.video_urls]
    if include_titles:
        titles = [
            f'{i:03d} - {get_title(video)}' for i, video in enumerate(playlist.videos, 1)]
    else:
        titles = [f'{i:03d} - {playlist.title}' for i in range(len(urls))]
    return zip(urls, titles)


@retry
def get_channel(url, include_titles=True):
    c = Channel(url)
    urls = [url.watch_url for url in reversed(c.video_urls)]
    print('URLS:')
    print(urls)
    if include_titles:
        titles = [
            f'{i:03d} - {get_title(video)}' for i, video in enumerate(reversed(c.videos), 1)]
        return zip(urls, titles)
    return zip(urls, titles)


@retry
def get_channel_url(video_url):
    return YouTube(video_url).channel_url + '/videos'


# @retry
# def download_audio(url, filename):
#     yt = YouTube(url, use_po_token=True)
#     print('1')
#     yt.streams.filter(
#         adaptive=True, file_extension='mp4', only_audio=True
#     ).order_by('abr').desc().first().download(filename=filename)
#     print(f"{url} was downloaded successfully")
