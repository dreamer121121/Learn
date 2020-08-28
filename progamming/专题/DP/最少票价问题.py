class Solution:
    def mincostTickets(self, days, costs):
        """
        dp[i]表示到第i天所需的最少的票价
        :param days:
        :param costs:
        :return:
        """
        dp = [0 for _ in range(days[-1]+1)]
        day_index = 0
        for i in range(1,len(dp)):
            if i != days[day_index]:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1]+costs[0],dp[i-7]+costs[1],dp[i-30]+costs[2])
        pass


