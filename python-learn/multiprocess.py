from multiprocessing import Pool,Process,Lock
from multiprocessing.managers import BaseManager

class DemoClass(object):
    def __init__(self):
        self.tmp = []
    def update(self,val):
        print(self.tmp)
        self.tmp.append(val)
    def show(self):
        return self.tmp

class MyManager(BaseManager):
    pass


def run(instance,val):
    instance.update(val)


def Manager2():
    m = MyManager()
    m.start()
    return m


def prompt(result):
    """
    run results will be trans to this callback function
    :param result:
    :return:
    """
    if result:
        print("prime factorization is over")


MyManager.register('DemoClass',DemoClass)

if __name__ == '__main__':
    manager = Manager2()
    em = manager.DemoClass()
    # lock = Lock()
    p = Pool()

    for i in range(10):
        p.apply_async(run,args=(em,i),callback=prompt)
    #
    p.close()
    p.join()

    # process = [Process(target=run,args=(em,i,lock)) for i in range(10)]
    # for p in process:
    #     p.start()
    # for p in process:
    #     p.join()

    print(em.show())
#理论上2和3版本都能用，对象能在多进程中共享传递，改变
# from multiprocessing import Process, Value, Lock
# from multiprocessing.managers import BaseManager
#
#
# class Employee(object):
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = Value('i', salary)
#         self.data = []
#
#     def increase(self):
#         self.salary.value += 100
#         self.data.append(self.salary.value)
#         print(self.data)
#
#     def getPay(self):
#         return self.name + ':' + str(self.salary.value)
#
#
# class MyManager(BaseManager):
#     pass
#
#
# def Manager2():
#     m = MyManager()
#     m.start()
#     return m
#
#
# MyManager.register('Employee', Employee)
#
#
# def func1(em, lock):
#     with lock:
#         em.increase()
#
#
# if __name__ == '__main__':
#     manager = Manager2()
#     em = manager.Employee('zhangsan', 1000)
#     lock = Lock()
#     proces = [Process(target=func1, args=(em, lock)) for i in range(10)]
#     for p in proces:
#         p.start()
#     for p in proces:
#         p.join()
#     print(em.getPay())