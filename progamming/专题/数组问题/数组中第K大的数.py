class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        mid = len(heap) // 2
        for i in range(mid,-1,-1):
            self.maintain_minheap(heap,i)
        print(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heap.pop(0)
                heap = [num] + heap
                self.maintain_minheap(heap,0)
            else:
                continue
        return heap
    def maintain_minheap(self,nums,i):
        length = len(nums)
        left = 2*i+1
        right = 2*i + 2
        minimum = i
        if left < length and nums[left] < nums[i]:
            minimum = left
        if right < length and nums[right] < nums[minimum]:
            minimum = right
        if i != minimum:
            nums[i],nums[minimum] = nums[minimum],nums[i]
            self.maintain_minheap(nums,minimum)
        else:
            return


s = Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))
