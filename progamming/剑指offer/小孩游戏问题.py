def LastRemaining_Solution(n, m):
    # write code here
    if m == 0:
        return None
    children = [[i, 0] for i in range(n)]
    j = 0
    while len(children) > 1:
        print("--len(children)--",len(children))
        for i in range(len(children)):
            if j == m:#控制j返零
                j = 0
            children[i][1] = j
            j += 1
        for eachone in children:
            if eachone[1] == m - 1 and len(children) > 1:
                children.remove(eachone)
    return children[0][0]
print(LastRemaining_Solution(5,3))