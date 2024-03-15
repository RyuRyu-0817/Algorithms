"""
hashmapで保存する
prevで前のローマ数字を記憶して、その組み合わせ次第で分岐をする
for文をlen(s)分回して、hashmap(s[i]) > hashnmap(s[i-1]) (次のローマ数字の値の方が大きければ)で分岐した方が、prev変数を使わないで済んだ

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        ans = 0
        prev = None
        for item in s:
            if ((item == 'V' or item == 'X') and prev == 'I') or ((item == 'L' or item == 'C') and prev == 'X') or ((item == 'D' or item == 'M') and prev == 'C'):
                ans -= hashmap[prev]
                ans += hashmap[item] - hashmap[prev]
            else:
                ans += hashmap[item]
            prev = item
        return ans
        