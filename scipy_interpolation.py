# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:12:40 2023

@author: Marko
"""

from scipy.interpolate import interp1d
import numpy as np
# 1d interpolate
xs = np.arange(10)
ys = 2*xs+1
interp_func = interp1d(xs,ys)
newarr = interp_func(np.arange(2.1,3,0.1))
print(newarr)

from scipy.interpolate import UnivariateSpline
# spline interpolate
xs = np.arange(10)
ys = xs**2+np.sin(xs)+1

interp_func = UnivariateSpline(xs, ys)
newarr = interp_func(np.arange(2.1,3,0.1))
print(newarr)

from scipy.interpolate import Rbf
# інтерполяція з радіальною базисною функцією

interp_func = Rbf(xs,ys)
newarr = interp_func(np.arange(2.1,3,0.1))
print(newarr)