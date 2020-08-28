class Solution:
    def maxCoins(self, nums):
        # reframe problem as before
        nums = [1] + nums + [1]
        n = len(nums)
        # dp will store the results of our calls
        dp = [[0] * n for _ in range(n)]
        # iterate over dp and incrementally build up to dp[0][n-1]
        for left in range(n-2, -1, -1):
            for right in range(left+2, n):
                print(left,right)
                # same formula to get the best score from (left, right) as before
                dp[left][right] = max(nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right] for i in range(left+1, right))
        return dp[0][n-1]
s = Solution()
print(s.maxCoins([3,1,5,8]))