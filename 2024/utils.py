# This is a file that contains utility functions
# Import this with "from utils import *"

import time

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OTHER = '\033[91m'
    CLEAR = '\033c'


def start_timer():
    global start_time
    start_time = time.time()
    
def print_timer():
    print("--- %s seconds ---" % round((time.time() - start_time), 4))