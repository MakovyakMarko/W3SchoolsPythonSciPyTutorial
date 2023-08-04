# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 12:58:13 2023

@author: Marko
"""

import numpy as np
from scipy.stats import ttest_ind
# ttest
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1,v2)
print(res)
# ttest
res = ttest_ind(v1,v2).pvalue
print("ttest pvalue:",res)

# kstest
from scipy.stats import kstest

v = np.random.normal(size=100)

res = kstest(v, 'norm')
print("kstest:",res)

from scipy.stats import describe
# статистичний опис даних
v = np.random.normal(size=100)
res = describe(v)
print(res)

# тести на нормалізацію (перекоси та ексцеси)
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)
print(skew(v))
print(kurtosis(v))

# дізнайємось, чи дані походять з нормалнього розподілу
from scipy.stats import normaltest

v = np.random.normal(size=100)
print(normaltest(v))
