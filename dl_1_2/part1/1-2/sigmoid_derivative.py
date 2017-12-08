#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 11:57
# @Author  : ChambersLiu
# @Software: PyCharm

import numpy as np


def sigmoid_devirative(x):
    s = 1.0 / (1 + np.exp(-x))
    return s * (1 - s)
