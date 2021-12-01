'''
Descripttion: kmp算法
Author: lishaogang
version: 
Date: 2021-12-01 10:36:26
LastEditors: lishaogang
LastEditTime: 2021-12-01 10:56:59
'''

def getMaxPre(s):
    '''
    返回最大前后缀和'''
    res  = 0
    le = len(s)
    for i in range(1, le):
        if s[:i] == s[le-i:]:
            res = max(res, i)
    return res

def getNext(s):
    '''
    获取next数组'''
    next = [-1, 0]
    for i in range(2, len(s)):
        next.append(getMaxPre(s[:i]))
    return next

def KMP(s1, s2):
    '''
    从s1中找到s2的位置'''

    if len(s1)<len(s2) or s1=="" or s2=="":
        return -1
    
    next = getNext(s2)
    i1, i2 = 0, 0
    while i1<len(s1) and i2<len(s2):
        if s1[i1]==s2[i2]:
            i1+=1
            i2+=1
        elif next[i2]==-1:
            i1+=1
        else:
            i2 = next[i2]
    
    return i1-i2 if i2==len(s2) else -1

if __name__ == "__main__":
    s1 = "abbabbabab"
    s2 = "babab"
    print(KMP(s1, s2))
