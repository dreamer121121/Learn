from common import Math
from numpy import *
import numpy as np
# 分三类时的效果
center1 = [0.67757, -0.35243, -0.27584]
center2 = [-0.54099, 0.91587, -0.31511]
center3 = [-0.61196, 0.95268, 1.31981]


def compute_distance(x):
    # 与第一类中心点的距离
    dist1 = np.linalg.norm(x - center1)
    dist2 = np.linalg.norm(x - center2)
    dist3 = np.linalg.norm(x - center3)
    return dist1, dist2, dist3


dist1, dist2, dist3 = compute_distance(np.array([-0.21, -0.94, -0.99]))
print(dist1, dist2, dist3)
