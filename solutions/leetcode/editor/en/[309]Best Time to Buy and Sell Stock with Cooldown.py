# You are given an array prices where prices[i] is the price of a given stock 
# on the iᵗʰ day. 
# 
#  Find the maximum profit you can achieve. You may complete as many 
# transactions as you like (i.e., buy one and sell one share of the stock multiple times) 
# with the following restrictions: 
# 
#  
#  After you sell your stock, you cannot buy stock on the next day (i.e., 
# cooldown one day). 
#  
# 
#  Note: You may not engage in multiple transactions simultaneously (i.e., you 
# must sell the stock before you buy again). 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 5000 
#  0 <= prices[i] <= 1000 
#  
#  Related Topics Array Dynamic Programming 👍 5150 👎 179


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        hold = 0
        buy = -prices[0]
        sell = 0

        for i in range(1, n):
            h = max(hold, sell)
            b = max(buy, hold - prices[i])
            s = b + prices[i]
            hold = h
            buy = b
            sell = s

        return max(hold, sell)
# leetcode submit region end(Prohibit modification and deletion)
