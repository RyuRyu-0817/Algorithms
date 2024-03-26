"""
注目要素まで、ループを内部で行い、注目要素とループ内での要素を比べて、注目要素の方が大きかったら
ansを更新するかどうかをmax関数で行う
"""
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [1] * len(nums)
        for i in range(1, len(ans)):
            for j in range(i):
                if nums[i] > nums[j]:
                    ans[i] = max(ans[i], ans[j]+1)
        
        return max(ans)