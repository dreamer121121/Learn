class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        string = ''
        for i in range(1,n+1):
            string += str(i)
        num = string.count('1')
        return num
s = Solution()
print(s.NumberOf1Between1AndN_Solution(13))
