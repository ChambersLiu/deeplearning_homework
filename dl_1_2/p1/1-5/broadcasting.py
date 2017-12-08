#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 15:38
# @Author  : ChangboLiu
# @Software: PyCharm

import numpy as np


def softmax(x):
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    x_softmax = x_exp / x_sum
    return x_softmax

if __name__ == '__main__':
    x = np.array([
        [9, 2, 5, 6, 7],
        [7, 5, 4, 8, 10]])
    print(softmax(x))