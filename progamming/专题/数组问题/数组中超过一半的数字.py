class Solution():
    def MoreThanHalfNum_Solution(self, numbers):
        #1.哈希表
        cnt = {}
        for num in numbers:
            if num not in cnt.keys():
                cnt[num] = 1
            else:
                cnt[num] += 1
        for key,value in cnt.items():
            if value > len(numbers) / 2.0:
                return key
        return 0
    def MoreThanHalfNum(self,numbers):
        current = numbers[0]
        cnt = 0
        for i in range(len(numbers)):
            if numbers[i] == current:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                current = numbers[i+1]
        return current if cnt > 0 else 0

s = Solution()
print(s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))

print(s.MoreThanHalfNum([1,2,3,2,2,2,5,4,2]))
