import functools
class Solution():
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        str_arr = []
        for i in range(len(numbers)):
            str_arr.append(str(numbers[i])) #转换为字符串加入到数组中。
        str_arr.sort(key=functools.cmp_to_key(self.mycmp))
        print(str_arr)
        result = int(''.join(str_arr))
        return result
    def mycmp(self,x,y):
        #自定义比较函数
        a = str(x)
        b = str(y)
        if int(b+a)<int(a+b):
            return 1
        else:
            return -1

s = Solution()
print(s.PrintMinNumber([3,32,321]))