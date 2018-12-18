from numpy import *
import numpy as np
import matplotlib.pyplot as plt
def loadDataset(filename):
    f = open(filename,'r')
    dataset = []
    labelset = []
    lines = f.readlines()
    print(len(lines))
    for line in lines:
        line = line.strip()
        line = line.split('\t')
        dataset.append(float(line[1]))
        labelset.append(float(line[-1]))
    print(dataset)
    print(labelset)
    return dataset,labelset


X,Y = loadDataset('ex0.txt')
X = np.array(X)
Y = np.array(Y)
plt.scatter(X,Y,c='r')
plt.xlim(0,1)
plt.ylim(3,5)
plt.xticks(np.arange(0,1.1,0.1))
plt.yticks(())
plt.show()