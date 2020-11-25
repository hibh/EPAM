import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def sum_f():
    with Pool(
        25
    ) as p:  # 25 is the minimum value in order to keep within 60 seconds(worst case)
        a = sum(p.map(slow_calculate, range(0, 501)))
    return a


time_start = time.time()
if __name__ == "__main__":
    sum_f()

time_finish = time.time()
time_executing = time_finish - time_start
assert time_executing <= 60
