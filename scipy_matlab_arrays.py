# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:05:53 2023

@author: Marko
"""

from scipy import io
import numpy as np
# експорт даних у формат Matlab
arr = np.arange(10)
io.savemat('arr.mat', {'vec':arr})
# імпорт даних із формату Matpab

arr = np.array([0,1,2,3,4,5,6,7,8,9])
io.savemat('arr.mat', {'vec':arr})

mydata = io.loadmat('arr.mat')
print(mydata)

# відобразити лише масів даних з Matlab
print(mydata['vec'])
# щоб масив не збільшувався на один вимір треба зробити наступне
mydata = io.loadmat('arr.mat', squeeze_me= True)
print(mydata['vec'])