from pathlib import Path
import sys
import moviepy.editor as mp

directory = "./"


def main(argv):
    extract_mp3()


def extract_mp3():
    files = Path(directory).glob("*.3gpp")
    for file in files:
        ##convert to Mp3...
        print("converting...", file.name)
        my_clip = mp.VideoFileClip(file.name)
        print("myclip...", my_clip)
        my_clip.audio.write_audiofile(file.name + ".mp3")


if __name__ == "__main__":
    main(sys.argv[1:100])
