'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-12-15 12:20:11
LastEditors: lishaogang
LastEditTime: 2021-12-15 12:27:59
'''

def combinationSum(candidates, target):
    candidates.sort()
    n = len(candidates)
    dp = [[[] for j in range(n+1)] for i in range(target+1)]

    for i in range(len(candidates)):
        dp[candidates[i]][i+1] = [[candidates[i]]]
    
    for i in range(1,target+1):
        for j in range(1, n+1):
            if  i-candidates[j-1]>0:
                for k in range(1, j+1):
                    if dp[i-candidates[j-1]][k] != []:
                        for r in dp[i-candidates[j-1]][k][:]:
                            dp[i][j].append(r+[candidates[j-1]])
    res  = dp[target][1]
    for x in dp[target][2:]:
        res+=x
    return res

if __name__ == "__main__":
    arr = [2,3,6,7]
    tar = 7
    res= combinationSum(arr, tar)    
    print(res)