import numpy as np
import matplotlib.pyplot as plt

# 目标函数:y=x^2+2*x+1
def func(x):
    return x**2 + 2 * x + 1


# 目标函数一阶导数也即是偏导数:dy/dx=2*x+2
def dfunc(x):
    return 2 * (x+1)


def cal_loss(x):  # 损失函数定义当前的x与最优解之间的距离
    return (x + 1) ** 2


def GD(x_start, df, epochs, lr):

    xs = []
    x = x_start
    xs.append(x_start)
    min_loss = 0.01
    i = 0
    loss = cal_loss(x)

    while i <= epochs and loss > min_loss:
        print("迭代次数：" + str(i + 1))
        dx = df(x)
        v = - dx * lr
        x += v
        i += 1
        xs.append(x)
        loss = cal_loss(x)
    return xs


def demo_GD():
    # 演示如何使用梯度下降法GD()
    line_x = np.linspace(-5, 5, 100)
    line_y = func(line_x)

    x_start = -5  # 从-5开始进行梯度下降
    epochs = 100  # 最大迭代次数

    lr = 0.99  # 学习速率
    x = GD(x_start, dfunc, epochs, lr=lr)
    x = np.array(x)
    print(x)
    print(x[-1])

    color = 'r'
    plt.plot(line_x, line_y, c='b')
    plt.plot(x, func(x), c=color, label='lr={}'.format(lr))
    plt.scatter(x, func(x), c=color)#画散点图
    plt.legend()
    plt.savefig('c.jpg')
    plt.show()




if __name__ == '__main__':
    demo_GD()
