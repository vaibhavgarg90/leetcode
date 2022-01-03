# In a town, there are n people labeled from 1 to n. There is a rumor that one 
# of these people is secretly the town judge. 
# 
#  If the town judge exists, then: 
# 
#  
#  The town judge trusts nobody. 
#  Everybody (except for the town judge) trusts the town judge. 
#  There is exactly one person that satisfies properties 1 and 2. 
#  
# 
#  You are given an array trust where trust[i] = [ai, bi] representing that the 
# person labeled ai trusts the person labeled bi. 
# 
#  Return the label of the town judge if the town judge exists and can be 
# identified, or return -1 otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2, trust = [[1,2]]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
#  
# 
#  Example 3: 
# 
#  
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 1000 
#  0 <= trust.length <= 10⁴ 
#  trust[i].length == 2 
#  All the pairs of trust are unique. 
#  ai != bi 
#  1 <= ai, bi <= n 
#  
#  Related Topics Array Hash Table Graph 👍 2780 👎 208


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # boundary condition
        if n == 1:
            return 1

        # contains set of all the people who do not trust anyone else
        # if there is any town judge, that should be the only person remaining in the set
        _set = {x for x in range(1, n + 1)}

        # k-v pair of trusted person and list of all the people trusting that person
        # if there is any town judge, then everyone else should trust that person
        _dict = {}

        # loop over the trust list and manipulate set and dict
        for t in trust:
            trusting_party = t[0]
            trusted_party = t[1]
            if trusting_party in _set:
                _set.remove(trusting_party)
            if trusted_party not in _dict:
                _dict[trusted_party] = []
            trusting_parties = _dict[trusted_party]
            trusting_parties.append(trusting_party)
            _dict[trusted_party] = trusting_parties

        if len(_set) != 1:
            return -1

        probable_town_judge = _set.pop()

        if probable_town_judge not in _dict or len(_dict[probable_town_judge]) != n - 1:
            return -1

        return probable_town_judge
# leetcode submit region end(Prohibit modification and deletion)
