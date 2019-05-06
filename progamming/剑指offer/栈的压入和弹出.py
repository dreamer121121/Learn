def IsPopOrder(self, pushV, popV):
    # write code here
    self.stack = []
    while popV:
        # popV中非空时要继续
        if not self.stack:
            self.stack.append(pushV.pop(0))
        if pushV and self.stack[-1] != popV[0]:
            self.stack.append(pushV.pop(0))
        elif self.stack[-1] == popV[0]:
            self.stack.pop()
            popV.pop(0)
        elif not pushV and self.stack[-1] != popV[0]:
            return False
    return True
print(IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))
