def StrToInt(s):
    if not s:
        return 0
    flag = 0
    if s[0] == '+' or s[0] == '-':
        if s[0] == '-':
            flag = 1
        s = s[1:]
    if s.isdigit():
        sum = 0
        for i in range(len(s)):
            sum += (ord(s[i]) - 48) * (10 ** (len(s) - 1 - i))
        if flag == 1:
            sum = -sum
        return sum
    else:
        return 0

print(StrToInt('+123'))