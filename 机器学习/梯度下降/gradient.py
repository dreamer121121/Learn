import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 绘图部分
r'''
def fun(x,y):
    z=(1-x)**2+100*(y-x**2)**2
    return z 
fig=plt.figure()
ax=Axes3D(fig)
x=np.arange(-1.5,3,0.5)
y=np.arange(-0.5,2,0.5)
X,Y=np.meshgrid(x,y)
ax.plot_surface(X,Y,fun(X,Y),rstride=1,cstride=1,cmap='rainbow')
plt.savefig('bananas.png')
plt.xlim(-1.5,3)
plt.ylim(-0.5,2)
plt.xlabel('x')
plt.ylabel('y')
'''


def cal_loss(x, y):
    
    return (1-x)**2+100*(y-x**2)**2


def gradient_x(x, y):
    return -2 + 2 * x - 400 * (y - x ** 2) * x


def gradient_y(x, y):
    return 200 * (y - x ** 2)


def gradient(iteras_max=10000, min_loss=0.001):
    loss = 10
    iteras = 1
    result = []
    x = 0
    y = 0  # 从0,0点出发
    error = [0, 0]
    stepsize = 0.001
    while iteras < iteras_max and loss > min_loss:
        error[0] = gradient_x(x, y)
        error[1] = gradient_y(x, y)
        # 更新x和y
        x -= error[0] * stepsize
        y -= error[1] * stepsize
        # 计算损失
        loss = cal_loss(x, y)
    result.append(x)
    result.append(y)
    return result, loss


if __name__ == '__main__':
    w, loss = gradient()
    print(w, loss)
