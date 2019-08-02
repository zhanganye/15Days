# -*- coding:utf-8 -*-
import numpy as np
import json
import time
import calendar

class Point():
    x = 0
    y = 0
    z = 0

def getData():
    tmp = Point()
    tmp.x = 10
    tmp.y = 8
    return tmp
def getTime():
    print(time.localtime(time.time()))
    print(time.asctime(time.localtime(time.time())))

def getCalendar():
    print(calendar.month(2019, 7))

if __name__ == '__main__':
    l = np.argmax([2,4,7,5])
    print(l)

