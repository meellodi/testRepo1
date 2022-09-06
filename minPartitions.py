import math


def minPartitions(n):
    a = 1
    for char in n:
        if int(char) > a:
            a = int(char)
    return a
