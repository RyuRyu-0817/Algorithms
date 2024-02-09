def isAnagram(string1,string2):
    """
        dの初期化でO(n^2)
        下のループは，一つ一つの文字に対しcountするのでO(n^2)
        O(n^2)
    """
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")

    if len(string1) != len(string2): return False

    d = {s: string1.count(s) for s in string1}

    for s2 in string2:
        if s2 in d and d[s2] == string2.count(s2):
            continue
        else:
            return False
    
    return True
        
def isAnagram(string1,string2): # 再回答
    """
        dの初期化でOn()
        下のループは, string1で増やして,sring2で減らしたら,
        二つの文字が同じだったら, dのバリューは最終的にすべての要素で
        プラマイゼロになる
        O(n)
    """
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")

    if len(string1) != len(string2): return False

    d = {chr(asc): 0 for asc in range(ord("a"), ord("z")+1)}

    for i in range(len(string1)):
        d[string1[i]] += 1
        d[string2[i]] -= 1
    
    return True if max(d.values()) == 0 and min(d.values()) == 0 else False


