#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 14:58
# @Author  : ChambersLiu
# @Software: PyCharm

import numpy as np


def normalizeRows(x):
    x_norm = np.linalg.norm(x, axis=1, keepdims=True)
    print(x_norm)
    x = x / x_norm
    return x


if __name__ == '__main__':
    x = np.array([
        [0, 3, 4],
        [1, 6, 4]
    ])
    normalized_x = normalizeRows(x)
    print(normalized_x)
