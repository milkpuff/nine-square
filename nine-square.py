# -*- coding: utf-8 -*-

'''
逆时针按顺序输出一个矩阵，矩阵必须是奇数阶

比如：

[[65 64 63 62 61 60 59 58 57]
 [66 37 36 35 34 33 32 31 56]
 [67 38 17 16 15 14 13 30 55]
 [68 39 18  5  4  3 12 29 54]
 [69 40 19  6  1  2 11 28 53]
 [70 41 20  7  8  9 10 27 52]
 [71 42 21 22 23 24 25 26 51]
 [72 43 44 45 46 47 48 49 50]
 [73 74 75 76 77 78 79 80 81]]

'''

import numpy as np


def nine_square(n=5):

    assert n % 2 == 1

    Right = 'r'
    Left = 'l'
    Up = 'u'
    Down = 'd'
    data = np.zeros((n, n)) * np.nan
    l = n**2
    start = int((n - 1) / 2)
    x, y = start, start
    direction = Right
    for i in range(1, l + 1):
        data[x, y] = i
        if direction == Up and x - 1 >= 0:
            x -= 1
            if np.isnan(data[x, y - 1]):
                direction = Left
        elif direction == Left and y - 1 >= 0:
            y -= 1
            if np.isnan(data[x + 1, y]):
                direction = Down
        elif direction == Down and x + 1 < n:
            x += 1
            if np.isnan(data[x, y + 1]):
                direction = Right
        elif direction == Right and y + 1 < n:
            y += 1
            if np.isnan(data[x - 1, y]):
                direction = Up

    data = data.astype(int)
    return data


if __name__ == '__main__':
    print(nine_squere(9))
