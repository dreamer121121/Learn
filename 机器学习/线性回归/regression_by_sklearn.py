from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
def loadDataset(filename):
    f = open(filename,'r')
    dataset = []
    labelset = []
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split('\t')
        dataset.append(float(line[1]))
        labelset.append(float(line[-1]))
    return dataset,labelset

def regression(X,Y):
    w=[]
    clf = linear_model.LinearRegression()
    Y=Y.tolist()
    clf.fit(X,Y)
    w.append(clf.intercept_)
    w.append(clf.coef_[0])
    return w

def fig(X,Y,w):
    Y1 = w[0] + w[1]*X
    plt.plot(X,Y1)
    plt.scatter(X,Y,c='r')
    plt.xlim(0,1)
    plt.ylim(2,5)
    plt.xticks(np.arange(0,1.1,0.1))
    plt.yticks(())
    plt.title(u"sklearn_regression")
    plt.savefig('sklearn.jpg')
    plt.show()


if __name__ == '__main__':
    X, Y = loadDataset('ex0.txt')
    X = np.array(X).reshape(-1,1)
    Y = np.array(Y)
    w = regression(X,Y)
    print("最优参数w：",w)
    fig(X,Y,w)