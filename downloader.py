from shared import *
import csv

if __name__ == '__main__':
    PLAYLIST = 'https://www.youtube.com/playlist?list=PLaySzQJTCO1lYWD7re003k-Pov6ZynWS-'
    FILE = 'data/playlist.tsv'
    VIDEO_URL = 'https://youtu.be/J4Wdy0Wc_xQ?list=PLblh5JKOoLUIE96dI3U7oxHaCAbZgfhHk'
    CHANNEL = 'https://www.youtube.com/channel/UCtYLUTtgS3k1Fg4y5tAhLbw/videos'

    # # get channel url
    # print(get_channel_url(VIDEO_URL))

    # # save data
    # data = get_playlist(PLAYLIST)
    # with open(FILE, 'w') as f:
    #     for url, title in data:
    #         f.write(f'{url}\t{title}\n')

    # load data from file and download videos
    with open(FILE, 'r') as f:
        data = csv.reader(f, delimiter="\t")

        for i, (url, title) in enumerate(data, start=88):
            download_video(url, f'{i:03d} - {title}')
    
    
    # download_audio('https://www.youtube.com/watch?v=NMjhKNFE_OA', 'mus1.mp4')