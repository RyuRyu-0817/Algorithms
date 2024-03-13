"""
上は自分の実装
ゴリ押しで累積和で解いた。前からの累積和と後ろからの累積和をとって同じところのindexを取得
下は解説見て解き直し。
左側は、等差数列の和の公式を使う。右側は、すべての合計に左側を引いて、注目数を足す
nまで行って、途中で和が同じになったらok
"""
class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = [i+1 for i in range(n)]
        s1 = [0]*n
        s2 = [0]*n
        for j in range(n):
            s1[j] = s1[j-1] + nums[j] if j != 0 else nums[j]
        for k in range(n-1, -1, -1):
            s2[k] = s2[k+1] + nums[k] if k != n-1 else nums[k]


        for l in range(n):
            if s1[l] == s2[l]:
                return l+1
        return -1
    
class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = [i+1 for i in range(n)]
        s = sum(nums)
        for j in range(1, n+1):
            left_sum = (j*(j+1))/2
            right_sum = s - left_sum + j
            print(left_sum, right_sum)
            if left_sum == right_sum:
                return j
        return -1
    
