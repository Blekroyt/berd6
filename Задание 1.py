#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import math
import sys

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))
    # Найти искомую сумму.
    s = 0
    b = 0
    for a in A:
        if a % 2 == 0:
            b = a * a
        elif a % 2 != 0:
            b = 2 * a
        print(b)
        continue
