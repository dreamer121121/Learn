# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:41:58 2018

@author: dreamer
"""
import numpy as np
np.random.seed(0)
x = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
print(x)
