#找出给定数组中第K大的数（本题也可转换为求数组中最大的K个数）(用快排的思想)
#时间复杂度为O(n)
def find_K(nums,K):
    pivot = nums[0]
    nums = [num for num in nums[1:] if num >= nums[0]]+[nums[0]]+[num for num in nums[1:] if num < nums[0]]
    index = nums.index(pivot)
    if index+1 == K:
        return pivot
    if index+1 < K:
        return find_K(nums[index+1:],K-1-index)
    elif index+1 > K:
        return find_K(nums[:index],K)
nums = [5,1,2,3,4]
print(find_K(nums,1))

#(维护一个小顶堆)

def maintain_heap(heap,i):
    if not heap:
        return
    left = 2*i +1
    right = 2*i+2
    minimum = i
    if left < len(heap) and heap[left] < heap[minimum]:
        minimum = left
    if right < len(heap) and heap[right] < heap[minimum]:
        minimum = right
    if minimum != i:
        heap[minimum],heap[i] = heap[i],heap[minimum]
        maintain_heap(heap,minimum)
    else:
        return

def search(nums,K):
    heap = nums[:K]
    left_nums = nums[K:]
    """建立一个小顶堆"""
    for i in range(len(heap)//2,-1,-1):
        maintain_heap(heap,i)
    """建立一个小顶堆"""
    for num in left_nums:
        if num > heap[0]:
            heap.pop(0)
            heap.insert(0,num)
        else:
            pass
    return heap[0]

nums = [5,1,2,3,4]
print(search(nums,5))




