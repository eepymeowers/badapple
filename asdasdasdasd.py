# this script only works if playsound is installed, use pip3 install playsound if it is not installed
# this script has major issues with speed on Windows due to the speed of Windows' console!!!


import os
import playsound

from time import sleep

def get_frames(some_dir):
    # get a list of entries in the directory
    entries = list(os.scandir(some_dir))
    # scandir gives results in an arbitrary order,
    # this sorts them to be in order.
    entries.sort(key = lambda x: x.name)

    for entry in entries:
        with open(entry.path, "r") as f:
            # yield the frame to the calling function
            yield f.read()


def main():
    wait_time_ms = 1000 / 34.5 # fps - 34.5 is the most accurate I could make it, it still isn't perfect but oh well
    frames_dir = "out" # path to directory where frames are
    # iterate over the generator function
    for frame in get_frames(frames_dir):
        # clear the screen, because we arent using ncurses
        os.system('cls' if os.name == 'nt' else 'clear')
        # print the frame, probably
        print(frame)
        # technically this makes the fps slightly lower
        # because it doesnt take into account time to 
        # read the file but thats far beyond what would be
        # reasonable to implement in python
        sleep(wait_time_ms / 1000) # convert to seconds
# bad apple!!!!!
playsound.playsound('badapple.mp3', False)
main()
