def GetLeastNumbers_Solution(tinput, k):
    print("--tinput--",tinput)
    print("--k--",k)
    # write code here、
    l = 0
    r = len(tinput)-1
    j = Partition(tinput, l, r,k)
    print("--j--",j)
    print("--input--",tinput)
    while True:
        if j == k:
            return tinput[0:k]
        elif j > k:
            print("兴趣点在我左边")
            j = Partition(tinput, l, j,k)
            print("--j--",j)
            print("--tinpu--",tinput)
        elif k > j:
            print("兴趣点在我右边")
            j = Partition(tinput, j + 1, r,k)
            print("--j--",j)
            print("--input--",tinput)


def Partition(array, l, r,k):
    pivot = array[k]
    print("--input array--",array)
    print("--pivot--",pivot)
    array[k], array[r] = array[r], array[k]
    j = l-1 #易错点
    print("--l,r--",l,r)
    for i in range(l, r):
        if array[i] < pivot:
            j += 1
            if j != i:
                array[j], array[i] = array[i], array[j]
    j += 1
    array[-1], array[j] = array[j], array[-1]

    return j

print(GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))


