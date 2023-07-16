import random
import time


def sleep(lower: float = 1.0, upper: float = 3.0):
    delay = random.uniform(lower, upper)
    time.sleep(delay)
