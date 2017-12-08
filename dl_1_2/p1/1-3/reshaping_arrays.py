#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 14:20
# @Author  : ChambersLiu
# @Software: PyCharm

import numpy as np


def image2vector(image):
    vec = image.reshape(image.shape[0] * image.shape[1] * image.shape[2], 1)
    return vec


if __name__ == '__main__':
    image = np.random.random(size=(3, 4, 5))
    print(image)
    print(image2vector(image))

