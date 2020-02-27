# def main():
#     a = 3
#     print('unchanged:'+str(a)+'\n')
#     change(a)
#     print('changed:'+str(a)+'\n')
#
# def change(a):
#     a += 1
#     print('changeing:',a)
#
# if __name__ == '__main__':
#     main()

#Python传参问题，一般变量的传递是值的传递，而可迭代对象的传递是地址的传递。
#
# a = [3]
# def change(a):
#     a.append(4)
#     print(a)
# print(a)
# change(a)
# print(a)
# # [3]
# # [3, 4]
# # [3, 4]
# a = 3
# def change(a):
#     a += 1
#     print(a)
# print(a)
# change(a)
# print(a)
# # 3
# # 4
# # 3
# #
