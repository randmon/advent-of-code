# This is a file that contains utility functions
# Import this with "from utils import *"

import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CLEAR = '\033c'


def start_timer():
    global start_time
    start_time = time.time()
    
def print_timer():
    print("--- %s seconds ---" % round((time.time() - start_time), 4))