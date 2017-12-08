#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/8 17:14
# @Author  : ChambersLiu
# @Software: PyCharm

import numpy as np


def l1_loss(y_hat, y):
    loss = np.sum(np.abs(y_hat - y))
    return loss


def l2_loss(y_hat, y):
    loss = np.sum(np.power(y_hat - y, 2))
    return loss


yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])

print("L1 loss = " + str(l1_loss(yhat, y)))
print("L2 loss = " + str(l2_loss(yhat, y)))
