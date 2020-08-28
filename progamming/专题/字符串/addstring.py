class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) == 1 and len(num2) == 1:
            return str(int(num1) + int(num2))
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        res = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        tmp = 0
        # 最终有多少位
        for i in range(len(num2)):
            ch1 = int(num1[i])
            ch2 = int(num2[i])
            if ch1 + ch2 + tmp >= 10:
                res.append(str(ch1 + ch2 - 10))
                tmp = 1
            else:
                res.append(str(ch1 + ch2))
                tmp = 0
        j = len(num2)
        while j < len(num1):
            ch = int(num1[j])
            if ch + tmp == 10:
                tmp = 1
                res.append("0")
                j += 1
            else:
                res.append(str(ch + tmp))
                tmp = 0
                break
        j += 1
        if tmp == 1:
            result = "".join(res) + num1[j:] + str(tmp)
        else:
            result = "".join(res) + num1[j:]
        result = result[::-1]
        return result
