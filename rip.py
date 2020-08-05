import sys
from pytube import YouTube, Playlist

SAVE_PATH = '~./Downloads/'

def main(argv):
    method = argv[0]
    url = argv[1]
    print('url ', url)
    # getUrl(url)
    functions.get(method)(url)

def ripSingleVideo(localurl):
    print("function running ripSingleVideo")
    # localurl = getURL()
    print("local url = ", localurl)
    try:
        yt = YouTube(localurl)
    except ConnectionError as e:
        print('Error: ', e)
    mp4files = yt.streams.first()
    mp4files.download(SAVE_PATH)

def ripList(localurl):
    print("function running rip list")
    #  localurl = getURL()
    print("local url = ", localurl)
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




