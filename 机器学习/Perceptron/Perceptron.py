import matplotlib.pyplot as plt
import numpy as np

def Perceptron(dataset):
    w=np.array([[0,0]],dtype='float64');b=0
    learn_rate = 1.0
    i = 0
    while i < len(dataset):
        flag = dataset[i,2]*(sum(dataset[i,:2]*w.reshape(-1))+b) <= 0
        if flag:
            print(i)
            w += learn_rate*dataset[i,:2]*dataset[i,2]
            b += learn_rate*dataset[i,2]
            i = 0
            continue
        i += 1
    return w,b

if __name__ == '__main__':
    # 绘制散点图
    plt.scatter([3, 4], [3, 3], c='red')
    plt.scatter([1], [1], c='black')
    dataset = np.array([[3, 3, 1], [4, 3, 1], [1, 1, -1]],dtype='float64')
    w,b = Perceptron(dataset)
    x = np.arange(0,10,1)
    plt.plot(x,-x-b,color='blue')
    plt.xlim(0, 5)
    plt.ylim(0,5)
    plt.show()
