from shared import *
import csv
if __name__ == '__main__':
    PLAYLIST_1 = 'https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9'
    PLAYLIST_2 = 'https://www.youtube.com/playlist?list=PLblh5JKOoLUIcdlgu78MnlATeyx4cEVeR'
    FILE_1 = 'data/playlist_1.txt'
    FILE_2 = 'data/playlist_2.txt'

    # playlist_1 = get_playlist(PLAYLIST_1, include_titles=False)
    # playlist_2 = get_playlist(PLAYLIST_2, include_titles=False)

    # # save data to files
    # for playlist, file in [(playlist_1, FILE_1), (playlist_2, FILE_2)]:
    #     with open(file, 'w') as f:
    #         f.write("\n".join(playlist))
    
    # load data from files and compare
    playlists = []
    for file in [FILE_1, FILE_2]:
        with open(file, 'r') as f:
            playlists.append(f.readlines())

    # print(len(playlists[0]))
    # print(len(playlists[1]))
    matches = [i in playlists[1] for i in playlists[0]]
    unique = [i for i in playlists[0] if i not in playlists[1]]
    print(len(unique))

