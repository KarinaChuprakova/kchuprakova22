#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing
import random

n = 10000

def pi(z):
    in_circle = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            in_circle += 1
        return in_circle
    
def test_all(pool):
    l = pool.map(pi, [1] * n)
    return l

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    print(test_all(pool))
    m = sum(test_all(pool))
    print((4 * m) / n)
else:
    print(__name__)
