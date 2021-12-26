# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
# k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
#  Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#  Example 2: 
#  Input: nums = []
# Output: []
#  Example 3: 
#  Input: nums = [0]
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics Array Two Pointers Sorting 👍 14905 👎 1427


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums = sorted(nums)
        size = len(nums)
        d = {}
        for i in range(0, size, 1):
            x = nums[i]
            if x > 0:
                break
            j = i + 1
            k = size - 1
            while j < k:
                y = nums[j]
                z = nums[k]
                if x + y > 0:
                    break
                _sum = x + y + z
                if _sum == 0:
                    if x not in d:
                        d[x] = {}
                    d[x][y] = z
                    j += 1
                elif _sum < 0:
                    j += 1
                else:
                    k -= 1
        l = []
        for k1, v1 in d.items():
            for k2, v2 in v1.items():
                l.append([k1, k2, v2])
        return l
# leetcode submit region end(Prohibit modification and deletion)
