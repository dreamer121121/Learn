a = [1,2,3,4,5,6,7]
target = 9
#1.两层循环，暴力破解
#2.还是暴力破解只是在寻找num2时利用num2 in list的特性加快搜索速度
#3.使用hash，将列表中的数的位置缓存在哈希表中,方法3利用哈希表可以O(1)找到num2,但是在建立哈希表时需要遍历整个列表多余了
def TwoSum(a,target):
    hash = {}
    for id,ele in enumerate(a):
        hash[ele] = id
    for i,ele in enumerate(a):
        j = hash.get(target-ele)
        if j != None and j != i:
            return [i,j]
# print(TwoSum(a,target))
#方法4是对方法3的改进，不需要遍历整个列表一遍建表一遍判断哈希表中是否有满足条件的值了，
def solution4(a,target):
    hash = {}
    for i,ele in enumerate(a):
        if hash.get(target-ele):
            return [hash.get(target-ele),i]
        hash[ele] = i
print(solution4(a,target))

