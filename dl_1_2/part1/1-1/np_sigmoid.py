#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 11:53
# @Author  : ChambersLiu
# @Software: PyCharm

import numpy as np


def np_sigmoid(x):
    s = 1.0 / (1 + np.exp(-x))
    return s


if __name__ == '__main__':
    x = np.array([1, 2, 3])
    print(np_sigmoid(x))
