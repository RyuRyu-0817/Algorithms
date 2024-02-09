def missingIntegers(numbers): #最初の解答
    """
        dの初期化でO(n), 次のループは配列の線形探索がn回行われるのでO(n^2)
        つまり,O(n^2)
    """

    d = {number: number for number in range(1, len(numbers)+1)}
    ans = []

    for key in d.values():
        if key in numbers:
            continue
        else:
            ans.append(key)
    
    return ans

def missingIntegers(numbers): #改良版
    """
        dの初期化でO(n), 次のループはハッシュマップの検索がn回なのでO(n)
        つまり,O(n)
    """
    d = {number: number for number in numbers}
    ans = []

    for target in range(1, len(numbers)+1):
        if target in d:
            continue
        else:
            ans.append(target)
    
    return ans
