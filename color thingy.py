#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 19:00:47 2022

@author: priyankadas
"""

import matplotlib.pyplot as plt

data =  [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

plt.imshow(data, cmap = "rainbow")

