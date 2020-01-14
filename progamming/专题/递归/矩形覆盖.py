#本质：斐波那契数列，关键在于找到规律。
class Solution():
    def rectCover(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        return self.rectCover(number-1)+self.rectCover(number-2)

s = Solution()
print(s.rectCover(2))