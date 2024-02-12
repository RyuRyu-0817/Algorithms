"""
stackに順に積んでいって,演算子にぶつかれば,二つstackからpopして
演算をする。それ以外は単にstackに積む
初期化の逆順でO(n), whileでO(n)
O(n)
"""
n = int(input())
a = input().split()[::-1]

stack = []

while a:
    t = a.pop()
    if t == "+":
        top = stack.pop()
        down = stack.pop()
        stack.append(int(top)+int(down))
    elif t == "-":
        top = stack.pop()
        down = stack.pop()
        stack.append(int(down)-int(top))
    else:
        stack.append(t)
print(stack[0])