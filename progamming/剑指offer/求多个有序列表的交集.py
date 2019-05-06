# 返回firstList 里的所有能在 secondList 里找到的元素
def getAllElementsInSencodList(firstList, secondList):
    list_c = [a for a in firstList if a in secondList]
    return list_c


def getIntersection(uinList):
    while len(uinList) > 1:
        list_a = []
        list_b = []
        list_a = uinList.pop()
        list_b = uinList.pop()
        list_c = getAllElementsInSencodList(list_a, list_b)
        if len(list_c) > 0:
            uinList.append(list_c)

    return uinList[0]

if __name__ == "__main__":
    print (getIntersection([[1,2,3,4],[2,3,4],[5,4,7,8]]))