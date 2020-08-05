import sys
from pytube import YouTube, Playlist

SAVE_PATH = '~./Downloads/'

def main(argv):
    if(len(argv) > 2):
        print('Error. Too many arguments')
        return
    else:
        method = argv[0]
        url = argv[1]
        functions.get(method)(url)

def ripSingleVideo(localurl):
    print('trying rip single video....')
    try:
        yt = YouTube(localurl)
    except ConnectionError as e:
        print('Error: ', e)
    mp4files = yt.streams.first()
    mp4files.download(SAVE_PATH)

def ripList(localurl):
    print('trying rip list....')
    try:
        playlist = Playlist(localurl)
        playlist.download_all(SAVE_PATH)
    except Exception as e:
        print('Error: ', e)

functions = {
    'single': ripSingleVideo,
    'list': ripList
}

if __name__ == "__main__":
   main(sys.argv[1:])




