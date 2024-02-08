"""
入力をリストで逆順化
リストのトップとスタックのトップを連結したものが、kindsに入っていたら、
スタックから除去。それを入力がなくなるまで繰り返す。
whileの終わりにstackが空だったら、true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        kinds = ("()", "{}", "[]")
        k = list(s)[::-1]
        stack = []
        stack.append(k.pop())

        while k:
            target = k.pop()
            if stack and stack[-1] + target in kinds:
                stack.pop()
                continue
            stack.append(target)
        
        return True if not stack else False
