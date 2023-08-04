# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 18:09:50 2023

@author: Marko
"""

# Розріджені дані: це набір даних, де більшість значень 
# елементів дорівнює нулю.

# Щільний масив: це протилежність розрідженому масиву: 
# більшість значень не дорівнюють нулю.

# Як працювати з розрідженими даними
# SciPy має модуль, scipy.sparse який надає функції для 
# обробки розріджених даних.

# В основному ми використовуємо два типи розріджених 
# матриць:

# CSC – стиснутий розріджений стовпець. Для ефективної 
# арифметики, швидке нарізання стовпців.

# CSR – стиснутий розріджений рядок. Для швидкого нарізання 
# рядків, швидші матричні векторні продукти

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))

arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
# перегляд ненульових елементів із властивістю data
print(csr_matrix(arr).data)
# підрахунок ненулів методом count_nonzero()
print(csr_matrix(arr).count_nonzero())
# видаленння нульових записів в матриці методом eliminate_zeros():
mat = csr_matrix(arr)
mat.eliminate_zeros()

print(mat)
# видалення повторюваних записів за допомогою sum_duplicates() методу
mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)
# перетворення з csr на csc за допомогою ticsc() методу:
newarr = csr_matrix(arr).tocsc()
print(newarr)