class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        cnt = {}
        for ele in s:
            if ele not in cnt.keys():
                cnt[ele] = 1
            else:
                cnt[ele] += 1
        for ele in s:
            if cnt[ele] == 1:
                return ele
            else:
                continue
        return -1
s = Solution()
print(s.FirstNotRepeatingChar('sdfdsfse'))