import functools
class Solution:
    def minNumber(self, nums):
        strs = [str(num) for num in nums]
        def compare(x,y):
            a,b = x+y,y+x
            if a > b:return 1
            elif a < b:return -1
            else:
                return 0
        strs.sort(key = functools.cmp_to_key(compare))
        result = ''.join(strs)
        return result
s = Solution()
print(s.minNumber([1,2,3]))