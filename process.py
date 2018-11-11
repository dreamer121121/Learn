import os
import json
import numpy as np
from numpy import *
from numpy import linalg as la

os.chdir(r'C:\Users\jack xia\Desktop\ARGUS\ARGUS\dianping')
f = open('results.txt', 'r')
content = json.load(f)
content = np.array(content,dtype=float)
content = content.Ts
content=mat(content)
u, sigma, vt = la.svd(content)
