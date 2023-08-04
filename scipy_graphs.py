# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 18:24:50 2023

@author: Marko
"""

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
# граф:
#   A
# 1/ \2
# B   C
# 
# arr = матриця суміжності:
#   A B C
# A 0 1 2
# B 1 0 0
# C 2 0 0
# Нижче наведено деякі з найбільш використовуваних методів
# роботи з матрицями суміжності
arr = np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
    ])
# Знайти всі зв'язані компоненти
newarr = csr_matrix(arr)
print(connected_components(newarr))

# Дейкстра - використовується, щоб знайти найкоротчий шлях
# у графі від одного елемента до іншого
from scipy.sparse.csgraph import dijkstra

print(dijkstra(newarr, return_predecessors=True, indices=0))

# Floyd Warshall() - метод, щоб знайти найкоротший шлях між
# усіма парами елементів
from scipy.sparse.csgraph import floyd_warshall

print(floyd_warshall(newarr, return_predecessors=True))

# Bellman Ford() - такий як Floyd метод, але цей метод можу 
# обробляти негативні ваги
from scipy.sparse.csgraph import bellman_ford
arr1 = np.array([
    [0,-1,2],
    [1,0,0],
    [2,0,0]
    ])
newarr1 = csr_matrix(arr1)
print(bellman_ford(newarr1,return_predecessors=True, indices=0)) 

# глибина першого порядку
from scipy.sparse.csgraph import depth_first_order

arr = np.array([
    [0,1,0,1],
    [1,1,1,1],
    [2,1,1,0],
    [0,1,0,1]
    ])
newarr = csr_matrix(arr)
print("глибина першого порядку:\n",depth_first_order(newarr,1))

# ширина першого порядку
from scipy.sparse.csgraph import breadth_first_order

print("ширина першого порядку:\n",breadth_first_order(newarr, 1))