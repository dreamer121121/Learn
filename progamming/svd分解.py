from numpy import *
import numpy as np
A= np.random.randn(3,5)
U,sigma,V = linalg.svd(A)
# print(A)
print("U",U)
print("V",V)
print("sigma",sigma)
