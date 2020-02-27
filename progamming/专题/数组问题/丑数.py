class Solution:
    def GetUglyNumber_Solution(self, index):
        #简单粗暴的方法，一个一个进行判断
        cnt = []
        i = 1
        while len(cnt) < index:
            if self.judge(i):
                cnt.append(i)
            i += 1
        return cnt[-1]

    def judge(self,num):
        while num%2 == 0:
            num = num // 2
        while num%3 == 0:
            num = num // 3
        while num%5 == 0:
            num = num //5
        if num == 1:
            return True
        return False

    def GetUglyNumber_Solution2(self, index):
        #利用丑数的性质生成一个丑数数列
        Ugly_array = [0]*index
        Ugly_array[0] = 1
        '''定义三个指针'''
        P2 = 0
        P3 = 0
        P5 = 0
        '''定义三个指针'''
        next_ugly_index = 1
        while next_ugly_index < index: #控制循环将Ugly_array填满
            min_num = min(Ugly_array[P2]*2,Ugly_array[P3]*3,Ugly_array[P5]*5)
            Ugly_array[next_ugly_index]=min_num
            while Ugly_array[P2]*2 <= Ugly_array[next_ugly_index]:
                P2 +=1
            while Ugly_array[P3]*3 <= Ugly_array[next_ugly_index]:
                P3 += 1
            while Ugly_array[P5]*5 <= Ugly_array[next_ugly_index]:
                P5 += 1
            next_ugly_index += 1
        return Ugly_array[-1]



s = Solution()
print(s.GetUglyNumber_Solution2(7))