#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 11:18
# @Author  : ChambersLiu
# @Site    : 
# @File    : sigmoid.py
# @Software: PyCharm
import math


def base_sigmoid(x):
    s = 1.0 / (1 + math.exp(-x))
    return s


if __name__ == '__main__':
    print(base_sigmoid(3))
