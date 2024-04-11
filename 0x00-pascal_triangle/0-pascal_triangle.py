#!/usr/bin/python3
'''A Create a function def pascal_triangle(n):.
'''


def pascal_triangle(n):
    '''This creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triang = []
    if type(n) is not int or n <= 0:
        return triang
    for i in range(n):
        lin = []
        for j in range(i + 1):
            if j == 0 or j == i:
                lin.append(1)
            elif i > 0 and j > 0:
                lin.append(triang[i - 1][j - 1] + triang[i - 1][j])
        triang.append(lin)
    return triang
