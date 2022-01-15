# You are given an integer array coins representing coins of different 
# denominations and an integer amount representing a total amount of money. 
# 
#  Return the fewest number of coins that you need to make up that amount. If 
# that amount of money cannot be made up by any combination of the coins, return -1.
#  
# 
#  You may assume that you have an infinite number of each kind of coin. 
# 
#  
#  Example 1: 
# 
#  
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#  
# 
#  Example 2: 
# 
#  
# Input: coins = [2], amount = 3
# Output: -1
#  
# 
#  Example 3: 
# 
#  
# Input: coins = [1], amount = 0
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 2³¹ - 1 
#  0 <= amount <= 10⁴ 
#  
#  Related Topics Array Dynamic Programming Breadth-First Search 👍 9568 👎 234


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, reverse=True)
        not_found = -1

        def memoization(f):
            _dict = {}

            def inner(amount, steps):
                if amount not in _dict or _dict[amount][0] > steps:
                    total_steps = f(amount, steps)
                    _dict[amount] = (steps, total_steps)
                return _dict[amount][1]

            return inner

        @memoization
        def rec(amount, steps):
            # print(f"{amount = }, {steps = }")
            if amount < 0:
                return not_found
            if amount == 0:
                return steps
            min_steps = _max = 10 ** 6
            for coin in coins:
                if coin <= amount:
                    total_steps = rec(amount - coin, steps + 1)
                    if total_steps != not_found:
                        min_steps = min(min_steps, total_steps)
            return min_steps if min_steps != _max else not_found

        if amount == 0:
            return 0
        return rec(amount, 0)
# leetcode submit region end(Prohibit modification and deletion)
