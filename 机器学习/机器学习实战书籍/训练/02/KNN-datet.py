import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn import preprocessing
from sklearn import neighbors
from sklearn.model_selection import cross_val_score
def main():
    os.chdir(r'C:\Users\jack xia\Desktop\连接公司\ARGUS\机器学习\机器学习实战书籍\训练\02')
    data=pd.read_csv('dataSet.csv').values
    train_data=data[0:899,1:5]
    test_data=data[900:999,1:5]
    train_X=train_data[:,0:3]
    train_y=train_data[:,3]
    test_X=test_data[:,0:3]
    test_y=test_data[:,3]
    #数据预处理(数据归一化)
    train_X=preprocessing.MinMaxScaler().fit_transform(train_X)
    test_X=preprocessing.MinMaxScaler().fit_transform(test_X)
    knn=neighbors.KNeighborsClassifier(n_neighbors=cross_val_k(train_X,train_y))
    knn.fit(train_X,train_y)
    scores=knn.score(test_X,test_y)
    print(scores)    
def cross_val_k(train_X,train_y):
    k_scores={}
    best_k=1
    for k in range(1,300):
        knn=neighbors.KNeighborsClassifier(n_neighbors=k)
        scores=cross_val_score(knn,train_X,train_y,cv=10,n_jobs=1)
        k_scores[k]=scores.mean()
    for key in k_scores:
        if k_scores[best_k]<=k_scores[key]:
            best_k=key
        else:
            continue
    return best_k

if __name__=='__main__':
    main()
#开始构建模型    
#按书上要求绘制图像

r'''
data_label=data[:,4].tolist()
Datelabel=[]
for each in data_label:
    if each =='didntLike':
        Datelabel.append(3)
    elif each == 'largeDoses':
        Datelabel.append(1)
    else:
        Datelabel.append(2)
draw_data=data[:,1:3]
matplotlib.rcParams['font.family']='SimHei'
plt.scatter(draw_data[:,0],draw_data[:,1],c=np.array(Datelabel))
plt.xlabel('飞行常客里程数')
plt.ylabel('玩游戏时间所耗时间所占比')
plt.savefig('picture1fly-play.jpg')
plt.close()
draw_data1=data[:,2:4]
plt.scatter(draw_data1[:,0],draw_data1[:,1],c=np.array(Datelabel),s=np.array(Datelabel))
plt.xlabel('玩游戏时间所耗时间所占比')
plt.ylabel('每周消耗冰激凌总数')
plt.savefig('picture2play-icecream.jpg')
'''



            
    

