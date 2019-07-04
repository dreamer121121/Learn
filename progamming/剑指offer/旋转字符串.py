def LeftRotateString(s, n):
    # write code here
    s_list = list(s)
    queue = []
    if n % len(s) == 0:
        return s
    else:
        for i in range(n):
            queue.append(s_list.pop(0))
        for j in range(len(queue)):
            s_list.append(queue.pop(0))
        result = "".join(s_list)
        return result
print(LeftRotateString(',6',1))
