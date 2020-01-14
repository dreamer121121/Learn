class Solution():
    def plusOne(self,digits):
        end = digits[-1]
        if end != 9:
            digits[-1] += 1
        else: #最后一位为9
            index_9 = len(digits)-1
            for i in range(len(digits)-2,-1,-1):
                if digits[i] == 9:
                    index_9 = i
                else:
                    break
            for i in range(index_9,len(digits)):
                digits[i] = 0
            if index_9 != 0:
                digits[index_9-1] += 1
            else:
                digits = [1]+digits
        return digits


s = Solution()
print(s.plusOne([9,9,9]))
