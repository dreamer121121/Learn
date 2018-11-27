
# coding: utf-8

# # K-Means及K-Medoid
# ## 1 算法简介
# 通常意义上接触的聚类问题是一个按照相似性（距离）进行样本聚集的过程，即把相似的（或距离近的）样本聚为同一类，而把不相似的（或距离远的）样本归在其他类。
# 
# 我们以一个二维的例子来说明聚类的目的。如下图左所示，假设我们的n个样本点分布在图中所示的二维空间。从数据点的大致形状可以看出它们大致聚为三个簇，其中两个紧凑一些，剩下那个松散一些。我们的目的是为这些数据分组，以便能区分出属于不同的簇的数据，如果按照分组给它们标上不同的颜色，就是像下图右边的图那样：
# ![fig1](./Img/fig1.png)
# 
# 我们知道，当人肉眼观察到上述的数据样本分布图的时候，很容易人工进行聚类。在机器学习中，我们运用k-means算法和k-medoid算法实现相类似的聚类工作。k-means算法是一种很常见的聚类算法，它的基本思想是：通过迭代寻找k个聚类的一种划分方案，使得用这k个聚类的均值来代表相应各类样本时所得的总体误差最小。
# 
# k-means算法的基础是最小误差平方和准则。其代价函数是：
# $$J(c,\mu) = \sum_{i=1}^k {\|x^{(i)}-\mu_{c(i)}\|}^2$$
#  
# 式中，$μ_{c(i)}$表示第$i$个聚类的均值。
# 
# 我们希望代价函数最小，直观的来说，各个簇内的样本越相似，那么簇内样本点与该簇均值间的误差平方和越小，不断调整簇的均值即means值，即可寻找到聚成$k$个簇时，最优的聚类方案。
# 

# ## 2 算法过程
# 
# 代价函数无法用解析的方法最小化，只能有迭代的方法。k-means算法是将样本聚类成 k个簇（cluster），其中k是用户给定的，其求解过程非常直观简单，具体算法描述如下：
# 
# 1、随机选取 k个聚类质心点
# 
# 2、重复下面过程直到$\mu_j$收敛  
# 
# {
# 
#   对于每一个样例 i，计算其应该属于的类：
# 
# $$c^{(i)} = arg \min_j {\|x^{(i)}-\mu_{j}\|}^2$$
# 
#    对于每一个类 j，重新计算该类的质心：
# $$\mu_j := \frac{\sum_{i=1}^{m}\{ c^{(i)} = j \} x^{(i)}}{\sum_{i=1}^{m}\{ c^{(i)} = j \}}$$
# 
# 
# }
# 
# 下图展示了对n个样本点进行K-means聚类的效果，这里k取2。$^{[2]}$
# 
# （a）在开始时，所有点都是绿色，表示初始样本点并未进行聚类划分
# 
# （b）指定2个means初始值，作为两个簇的初始均值，分别染色成红色和蓝色
# 
# （c）计算所有点到两个均值点的距离，根据距离的远近判断该点在第一次聚类所属的簇，若离红点近，则被聚类到红色的簇内。否则，被聚类到蓝色的簇内，此时所有点都被聚到两个簇内
# 
# （d）重新计算红蓝两个簇的均值，作为新的簇的均值点。
# 
# （e）基于新的均值点重复(c)(d)两个过程，直至均值点不再发生改变为止（收敛），聚类完成
# ![fig2](./Img/fig2.png)

# ## 3 代码分析
# k-means算法思路总体而言比较简单，但也有几个比较大的缺点：
# 
# (1) k值的选择是用户指定的，不同的k得到的结果有时会产生很大的不同，如下图所示，左边是k=3的结果，红色簇内数据点过于稀疏，而蓝色簇其实是可以再划分成两个簇的。而右图是k=5的结果，此时红色簇和蓝色簇又可以合并成一个簇：
# ![fig3](./Img/fig3.png)
# (2) 对k个初始质心的选择比较敏感，容易陷入局部最优解。例如，在上述算法运行时，有可能会在K-means收敛时，收敛到了局部最优值：
# ![fig4](./Img/fig4.png)
# (3) 存在局限性，非球状的数据分布不适合用K-Means聚类：
# ![fig5](./Img/fig5.png)
# (4) 数据量比较大的时候，收敛过程会比较慢。

# ## 4 代码实现
# 下面进行k-means算法的代码实现，首先导入相关的库函数：

# In[1]:


# get_ipython().run_line_magic('matplotlib', 'inline')
#
# from numpy import *
# import time
# import matplotlib.pyplot as plt


# 建立相关的功能函数实现聚类功能：

# In[2]:


# euclDistance函数计算两个向量之间的欧氏距离
# def euclDistance(vector1, vector2):
#     return sqrt(sum(power(vector2 - vector1, 2)))
#
# # initCentroids选取任意数据集中任意样本点作为初始均值点
# # dataSet: 数据集， k: 人为设定的聚类簇数目
# # centroids： 随机选取的初始均值点
# def initCentroids(dataSet, k):
#     numSamples, dim = dataSet.shape
#     centroids = zeros((k, dim))
#     for i in range(k):
#         index = int(random.uniform(0, numSamples))
#         centroids[i, :] = dataSet[index, :]
#     return centroids

# kmeans: k-means聚类功能主函数
# 输入：dataSet-数据集，k-人为设定的聚类簇数目
# 输出：centroids-k个聚类簇的均值点，clusterAssment－聚类簇中的数据点
# def kmeans(dataSet, k):
#     numSamples = dataSet.shape[0]
#
#     clusterAssment = mat(zeros((numSamples, 2)))
#     # clusterAssment第一列存储当前点所在的簇
#     # clusterAssment第二列存储点与质心点的距离
#     clusterChanged = True
#
#     ## 步骤一: 初始化均值点
#     centroids = initCentroids(dataSet, k)
#
#     while clusterChanged:
#         clusterChanged = False
#         ## 遍历每一个样本点
#         for i in range(numSamples):
#             # minDist：最近距离
#             # minIndex：最近的均值点编号
#             minDist  = 100000.0
#             minIndex = 0
#             ## 步骤二: 寻找最近的均值点
#             for j in range(k):
#                 distance = euclDistance(centroids[j, :], dataSet[i, :])
#                 if distance < minDist:
#                     minDist  = distance
#                     minIndex = j
#
#             ## 步骤三: 更新所属簇
#             if clusterAssment[i, 0] != minIndex:
#                 clusterChanged = True
#                 clusterAssment[i, :] = minIndex, minDist ** 2
#
#         ## 步骤四: 更新簇的均值点
#         for j in range(k):
#             print(clusterAssment[:, 0].A)
#             pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
#
#             centroids[j, :] = mean(pointsInCluster, axis=0)
#
#     print ('Congratulations, cluster complete!')
#     return centroids, clusterAssment
#
# # showCluster利用pyplot绘图显示聚类结果（二维平面）
# # 输入:dataSet-数据集，k-聚类簇数目，centroids-聚类簇的均值点，clusterAssment－聚类簇中数据点
# def showCluster(dataSet, k, centroids, clusterAssment):
#     numSamples, dim = dataSet.shape
#     if dim != 2:
#         print ("Sorry, the dimension of your data is not 2!")
#         return 1
#
#     mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
#     if k > len(mark):
#         return 1
#
#     # 画出所有的样本点
#     for i in range(numSamples):
#         markIndex = int(clusterAssment[i, 0])
#         plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])
#
#     mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
#     # 标记簇的质心
#     for i in range(k):
#         plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)
#
#     plt.show()
#
#
# # 在主函数中执行聚类操作：
#
# # In[3]:
#
#
# ## step 1: 载入数据
# if __name__ == '__main__':
#     dataSet = []
#     fileIn = open('./Data.txt')
#     for line in fileIn.readlines():
#         lineArr = line.strip().split('\t')
#         dataSet.append([float(lineArr[0]), float(lineArr[1])])
#
#     ## step 2: 开始聚类...
#     dataSet = mat(dataSet)
#     k = 4
#     centroids, clusterAssment = kmeans(dataSet, k)
#
#     ## step 3: 显示聚类结果
#     showCluster(dataSet, k, centroids, clusterAssment)
#


from numpy import *
import _pickle as cPickle
from matplotlib import pyplot as plt
from numpy import zeros, array, tile
from scipy.linalg import norm
import numpy.matlib as ml
import random



def euclDistance(vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))


def update_medoids(pointsInCluster):

    minsum = 100000
    minindex=0
    for i in range(len(pointsInCluster)):
        medoids = pointsInCluster[i]
        sum = 0
        for eachpoint in pointsInCluster:  # 计算该簇每一个点到medoids的距离
            sum += euclDistance(eachpoint, medoids)
        if sum < minsum:
            minsum = sum
            minindex = i

    return pointsInCluster[minindex]


def initCentroids(dataSet, k):
    numSamples, dim = dataSet.shape
    medoids = zeros((k, dim))
    for i in range(k):
        index = int(random.uniform(0, numSamples))
        medoids[i, :] = dataSet[index, :]
    return medoids

def kmedoids(dataset,k):
    numSamples = dataSet.shape[0]

    clusterAssment = mat(zeros((numSamples, 2)))  # 用于记录每一个样本所属的类别和距离本簇中心的距离

    ## 步骤一: 初始化medoids点
    medoids = initCentroids(dataSet, k)
    medoidsChanged = True

    while medoidsChanged:
        medoidsChanged = False

        ## 遍历每一个样本点
        for i in range(numSamples):
            # minDist：最近距离
            # minIndex：最近的均值点编号
            minDist = 100000.0
            minIndex = 0

            ## 步骤二: 寻找最近的medoids
            for j in range(k):
                distance = euclDistance(medoids[j, :], dataSet[i, :])
                if distance < minDist:
                    minDist = distance
                    minIndex = j

            ## 步骤三: 更新第i个样本所所属簇
            if clusterAssment[i, 0] != minIndex:
                clusterAssment[i, :] = minIndex, minDist ** 2

        ## 步骤四: 更新每个簇的中心点medoids
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]  # 取出所有属于同一类的样本点
            new_medoids = update_medoids(pointsInCluster).A  # 计算新的medoids

            # print("更新前的medoids", medoids[j, :])
            # print(type(medoids))
            # print("更新后的medoids", new_medoids)
            # print(type(new_medoids))
            # print(new_medoids[0,0])
            if new_medoids[0, 0] != medoids[j, 0] or new_medoids[0, 1] != medoids[j, 1]:
                medoidsChanged = True
                medoids[j, :] = new_medoids
        # print("------------------------------")
    print('Congratulations, cluster complete!')
    return medoids, clusterAssment

def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print ("Sorry, the dimension of your data is not 2!")
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        return 1

    # 画出所有的样本点
    for i in range(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # 标记簇的质心
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)

    plt.show()

if __name__ == '__main__':
    dataSet = []
    fileIn = open('./Data.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split('\t')
        dataSet.append([float(lineArr[0]), float(lineArr[1])])
    dataSet = mat(dataSet)
    k = 4

    # 调用kmedoids算法
    medoids, clusterAssment = kmedoids(dataSet, k)
    print(medoids)

    # step 3: 显示聚类结果
    showCluster(dataSet, k, medoids, clusterAssment)