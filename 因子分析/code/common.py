import numpy as np


class Math():
    def distance(self, vec1, vec2):  # 外部调用该方法时传参
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        dist = np.sqrt(np.sum(np.square(vec1 - vec2)))
        return dist


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):  # 进栈
        self.stack.insert(0, value)

    def pop(self):  # 出栈
        if self.stack:
            self.stack.pop(0)
        else:
            raise LookupError("stack is empty")

    def is_empty(self):  # 如果栈为空
        return bool(self.stack)

    def top(self):
        # 取出目前stack中最新的元素
        return self.stack[-1]
