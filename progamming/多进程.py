#方法一 直接调用import time
import time
import random
from multiprocessing import Process
def run(name):
    print('%s runing' %name)
    time.sleep(random.randrange(1,5))
    print('%s running end' %name)


if __name__ == '__main__':
    p1=Process(target=run,args=('anne',)) #必须加,号
    p2=Process(target=run,args=('alice',))
    p3=Process(target=run,args=('biantai',))
    p4=Process(target=run,args=('haha',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主线程')