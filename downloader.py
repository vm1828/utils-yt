from shared import *
import csv

if __name__ == '__main__':
    PLAYLIST = ''
    FILE = 'data/playlist.tsv'
    VIDEO_URL = ''
    CHANNEL = ''

    # # get channel url
    # print(get_channel_url(VIDEO_URL))

    # save data
    # data = get_playlist(PLAYLIST, include_titles=True)
    data = get_channel(CHANNEL, include_titles=True)
    with open(FILE, 'w') as f:
        for url, title in data:
            f.write(f'{url}\t{title}\n')

    # load data from file and download videos
    with open(FILE, 'r') as f:
        data = csv.reader(f, delimiter="\t")

        # for i, (url, title) in enumerate(data, start=1):
        #     download_video(url, f'{i:03d} - {title}')

        for (url, title) in data:
            download_video(url, title)