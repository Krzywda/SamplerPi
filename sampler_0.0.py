import os
import sys

def play_file(filename):
    os.system('aplay {filename}')
    return 0

play_file(sys.argv)
