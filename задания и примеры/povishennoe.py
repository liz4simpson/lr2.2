#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

EPS = 1e-10
if __name__ == '__main__':
    x = float(input("Value of x? "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)
    n = float(input("Value of n -> "))
    q = (x / 2) ** n

    a = x
    S, k = a, 1
    while math.fabs(a) > EPS:
        a *= (4 * k * math.factorial(k + 1 + n) + 4 * math.factorial(k + 1 + n)) / \
             math.factorial(k - 1) * math.factorial(k + n) * (x ** 2)
        S += a
        k += 1
    print(int(S))
