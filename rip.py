import sys
from pytube import YouTube, Playlist
from urllib.error import HTTPError

SAVE_PATH = "~./Downloads/"


def main(argv):
    if len(argv) > 2:
        print("Error. Too many arguments")
        return
    else:
        method = argv[0]
        url = argv[1]
        print("method?", method)
        print("url?", url)
        functions.get(method)(url)


def ripSingleVideo(localurl):
    print("trying rip single video....")
    try:
        yt = YouTube(localurl)
    except HTTPError as err:
        print("Http Error..", err)
    except ConnectionError as e:
        print("Error: ", e)
    mp4files = yt.streams.first()
    mp4files.download(SAVE_PATH)


def ripList(localurl):
    print("trying rip list....")
    try:
        p = Playlist(localurl)
        print("hit each video...", p.playlist_url)
        for video in p.videos:
            ## below print statement only prints the first video title....
            print("downloading...", p.title)
            video.streams.first().download()
        print(p)
    except Exception as e:
        print("Error: ", e)


functions = {"single": ripSingleVideo, "list": ripList}

if __name__ == "__main__":
    main(sys.argv[1:100])

