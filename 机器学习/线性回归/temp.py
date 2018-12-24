import numpy as np

w0 = np.arange(-5, 5, 0.1)
w1 = np.arange(-5, 5, 0.1)
w0, w1 = np.meshgrid(w0, w1)
print(w0.shape)
print(w1)
