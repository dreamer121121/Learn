# def main():
#     a = [1]
#     fun1(a)
#     print("--a--",a)
#
# def fun1(b): #传递的是地址！！！，在fun1中对数组a进行操作，会改编在main函数中的数组a
#     a = []
#     a.append(3)
#     b.append(2)
#     print("a",a)
#     print("b",b)
#
# main()
#----------------------注意区分这两种情况！！！当传递的数组时，传递的是地址(内层函数可以该碧昂上层函数定义的数组)，
#而当传递的是变量时，传递的是值的拷贝(即内层函数不能改变上层函数的变量值)
#格外注意 这样的使用方式并非是函数的嵌套！！！！！
# def main():
#     a = 1
#     fun1(a)
#     print("--a--",a)
#
# def fun1(b):
#     b = 2
#     print("--fun1 a--",b)
#
# main()


def main():
    a = 1
    fun1(a)
    print("--a--",a)

def fun1(b):
    b = 2
    print("--fun1 a--",b)

main()



# a = 1
# def main():
#     """
#     python的shadow机制
#     函数中可以引用q全局变量，但不能改变全局变量的值。
#     若想改变则需加 global
#     :return:
#     """
#     a = 2
#     print("--a--",a)
#
# main()
# print("---global a---",a)




