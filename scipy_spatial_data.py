# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:20:45 2023

@author: Marko
"""

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

# триангуляція 
points = np.array([
    [2,4],
    [3,4],
    [3,0],
    [2,2],
    [4,1]
    ])
simplices = Delaunay(points).simplices

plt.triplot(points[:,0], points[:,1], simplices)
plt.scatter(points[:,0], points[:,1], color='r')
plt.show()

# ConvexHull() - найменший багатокутник, який покриває всі задані точки
from scipy.spatial import ConvexHull
points = np.array([
    [2,4],
    [3,4],
    [3,0],
    [2,2],
    [4,1],
    [1,2],
    [5,0],
    [3,1],
    [1,2],
    [0,2]
    ])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0],points[:,1])
for simplex in hull_points:
    plt.plot(points[simplex,0],points[simplex,1],'k-')
    
plt.show()

# KDTrees - це  структура даних, 
# оптимізована для запитів найближчих сусідів
from scipy.spatial import KDTree
points = [(1,-1),(2,3),(-2,3),(2,-3)]
kdtree = KDTree(points)
res = kdtree.query((1,1))
print(res)

# матриця відстаней. Наприклад "К найближчих сусідів"
# еквклідова відстань
from scipy.spatial.distance import euclidean
p1 = (1,0)
p2 = (10,2)
res = euclidean(p1, p2)
print(res)
# відстань міського кварталу
from scipy.spatial.distance import cityblock
res = cityblock(p1, p2)
print(res)
# косинусна відстань
from scipy.spatial.distance import cosine
res = cosine(p1,p2)
print(res)
# відстань Хемінга
# це частка бітів, де два біти різні.
from scipy.spatial.distance import hamming
p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)
print(res)