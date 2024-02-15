"""
パイプの切り方を工夫した結果、切り出すことができるパイプの長さの最大値を答える
外のループはO(log(right-left))
内部ループはO(n)
よってO(nlog(right-left))
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, max(a)

while right - left > 1e-6:
    mid = (left+right)/2
    s = 0
    for ai in a:
        s += ai//mid
    
    if s >= k:
        # パイプの本数が予定より超過するということはまだ余裕をもって切れるということ
        # だから,長さを大きくして探索
        left = mid
    else:
        right = mid

print(mid)
