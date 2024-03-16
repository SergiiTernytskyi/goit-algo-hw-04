import sys 
from processing import show_directory

if len(sys.argv) > 1:
    path = sys.argv[2]

show_directory(path)