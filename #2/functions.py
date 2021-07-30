import pygame
import time
from math import *

from config import *

cur_time = time.time_ns()
def delta_time():
    global cur_time
    delta = (time.time_ns() - cur_time) / 1000000000
    cur_time = time.time_ns()
    return delta

