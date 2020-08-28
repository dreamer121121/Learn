# def pow(num):
# #     for i in range(num):
# #         yield i**2
#
# a = pow(5)
# print(a)
# """
# 生成器是可以迭代的
# """
# # for num in a:
# #     print(num)
# iter(a) #调用iter方法返回迭代器对象
# print(a.__next__())
# print(a.__next__())

"""自己实现一个迭代器"""
class myEven:
    def __init__(self, n):
        self.n = n
        self.num = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.n:
            value = self.num
            self.num += 2
            return value
        else:
            raise StopIteration
a = myEven(10)
a = iter(a)
print(a.__next__())
print(a.__next__())