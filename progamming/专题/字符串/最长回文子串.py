class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        f = [[0 for i in range(length)] for j in range(length)]
        for i in range(length - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])

