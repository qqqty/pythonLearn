import time
import math
import random

def cal(num):
    hit = 0
    for i in range(1, num+1):
        x, y = random.random(), random.random()

        r = math.sqrt(pow(x, 2) + pow(y, 2))

        if r < 1:
            hit += 1

    return float(4 * hit)/num

print time.localtime(time.time())

print time.strftime('%Y-%m-%d %H:%I:%S', time.localtime(time.time()+6*3600))
setNum = int(raw_input("num:"))

print cal(setNum)