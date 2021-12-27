# Given an array nums of n integers, return an array of all the unique 
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that: 
# 
#  
#  0 <= a, b, c, d < n 
#  a, b, c, and d are distinct. 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics Array Two Pointers Sorting 👍 5035 👎 601


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        size: int = len(nums)
        _map: dict = {}  # for dedup
        nums = sorted(nums)
        # print(f"nums :: {nums}")
        for i in range(0, size - 2, 1):
            a = nums[i]
            for j in range(i + 1, size - 1, 1):
                b = nums[j]
                k = j + 1
                l = size - 1
                while k < l:
                    c = nums[k]
                    d = nums[l]
                    _sum = a + b + c + d
                    if _sum == target:
                        # print(f"found match :: {i}, {j}, {k}, {l}")
                        if a not in _map:
                            _map[a] = {}
                        if b not in _map[a]:
                            _map[a][b] = {}
                        _map[a][b][c] = d
                        k += 1
                    elif _sum < target:
                        k += 1
                    else:
                        l -= 1
        # print(f"map :: {_map}")
        res: List[List[int]] = []
        for k1, v1 in _map.items():
            for k2, v2 in v1.items():
                for k3, v3 in v2.items():
                    res.append([k1, k2, k3, v3])
        return res
# leetcode submit region end(Prohibit modification and deletion)
