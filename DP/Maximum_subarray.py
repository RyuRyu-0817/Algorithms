"""
kadaneのアルゴリズム
今までの和dp[i-1]と現在の配列の値nums[i]の和と現在の配列の和を比べたとき、現在の方が
大きかったら、dp[i]を現在に更新
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i-1] + nums[i] < nums[i]:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]

        return max(dp)
            
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))