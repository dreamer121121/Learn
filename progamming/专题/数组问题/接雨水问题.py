class Solution:
    """
    暴力法O(N2)
    """
    def __init__(self):
        self.result = []
        self.length = 0
        self.height = []

    def trap(self,height):
        self.height = height
        self.length = len(height)
        if len(height)<3:
            return 0
        for i in range(1,len(height)-1):
            current_h = height[i]
            leftMax = self.maxleft(i)
            rightMax = self.maxright(i)
            res = max(min(leftMax,rightMax)-current_h,0)
            self.result.append(res)
        return sum(self.result)


    def maxleft(self,center):
        maxl = 0
        for i in range(center-1,-1,-1):
            if self.height[i] > maxl:
                maxl = self.height[i]
        return maxl

    def maxright(self,center):
        maxr = 0
        for i in range(center+1,self.length):
            if self.height[i] > maxr:
                maxr = self.height[i]
        return maxr


s=Solution()
print(s.trap( [0,1,0,2,1,0,1,3,2,1,2,1]))



