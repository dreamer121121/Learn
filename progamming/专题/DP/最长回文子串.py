class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        n = len(s)
        # 动态规划算法
        dp = [[1 for _ in range(n)] for _ in range(n)]
        sta = 0
        end = 0
        max_l = 1
        for i in range(n - 1, -1 , -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                #注意i=j-1的情况，此时i+1>j-1,因此需要将dp数组初始化为1来解决。
                dp[i][j] = (s[i] == s[j]) & dp[i + 1][j - 1]
                # 保留最大值，基于上述遍历规则，此处保留的为最右端的最长子串；如果求最左端的，将下述的<变为<=即可
                if dp[i][j] and max_l < j - i + 1:
                    max_l = j - i + 1
                    sta = i

        return s[sta:max_l + sta]
