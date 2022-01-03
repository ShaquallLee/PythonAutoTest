'''
Descripttion: 给一组不同面额的硬币，求使用最少的硬币来组成X元
Author: lishaogang
version: 
Date: 2021-12-06 18:15:24
LastEditors: lishaogang
LastEditTime: 2021-12-31 16:31:06
'''


def coinAdd(coins, index, rest):
    '''
    普通递归'''
    if rest < 0:
        return -1
    if rest == 0:
        return 0
    if index >= len(coins):
        return -1

    r1 = coinAdd(coins, index+1, rest)
    r2 = coinAdd(coins, index+1, rest-coins[index])
    if r1 == -1 and r2 == -1:
        return -1
    else:
        if r1 == -1:
            return 1+r2
        if r2 == -1:
            return r1
        return min(r1, 1+r2)


def coinAdd2(coins, index, rest, dp):
    '''
    加上记忆单元的递归'''
    if dp[index][rest] != -2:
        return dp[index][rest]
    if rest < 0:
        return -1
    if rest == 0:
        dp[index][rest] = 0
        return 0
    if index >= len(coins):
        return -1

    r1 = coinAdd2(coins, index+1, rest, dp)
    r2 = coinAdd2(coins, index+1, rest-coins[index], dp)
    if r1 == -1 and r2 == -1:
        dp[index][rest] = -1
        return -1
    else:
        if r1 == -1:
            dp[index][rest] = 1+r2
            return 1+r2
        if r2 == -1:
            dp[index][rest] = r1
            return r1
        dp[index][rest] = min(r1, 1+r2)
        return dp[index][rest]


def coinAdd3(coins, rest):
    '''
    动态规划的方法
    params：
        coins：硬币面值列表
        rest：需要组成的金额数
    others：
        转移矩阵dp中，行是硬币取或不取， 列是组成的金额
        第i行第j列的值表示的是从第i+1个金币开始使用，所组成金额j所需的最少硬币数量
        dp初始化时：
            第0列表示组成金额0的硬币数，所需硬币为0，故直接初始化为0
            第len(coins)+1行表示的是使用从不使用硬币（没有硬币可用）所组成的对应金额所需的
                数量，只有金额0的时候为0，其它的金额都是无法组成的，故都初始化为-1
    '''
    l = len(coins)
    dp = [[-2]*11 for i in range(l+1)]
    for i in range(l):
        dp[i+1][0] = 0
    for i in range(10):
        dp[l][i+1] = -1
    for i in range(l):
        for j in range(10):
            r1 = dp[l-i][j+1]
            if j+1-coins[l-i-1] < 0:
                dp[l-i-1][j+1] = r1
            else:
                r2 = dp[l-i][j+1-coins[l-i-1]]
                if r1 == -1 and r2 == -1:
                    dp[l-i-1][j+1] = -1
                else:
                    if r1 == -1:
                        dp[l-i-1][j+1] = r2+1
                    elif r2 == -1:
                        dp[l-i-1][j+1] = r1
                    else:
                        dp[l-i-1][j+1] = min(r1, r2+1)
    return dp[0][rest]


def coinAdd4(coins, num):
    '''
    通过无限数量的coins中的硬币面额，组成价值为num的值，
    求总共有多少种组合方法
    '''
    dp = [[0]*(num+1) for i in range(len(coins))]
    for i in range(len(coins)):
        dp[i][coins[i]]=1
    for i in range(len(coins)):
        for j in range(coins[i]+1, num+1):
            for k in range(i+1):
                if j-coins[i]>0:
                    dp[i][j] += dp[i-k][j-coins[i]]
    res = 0
    for i in range(len(coins)):
        res+=dp[i][num]
    return res

def coinAdd5(coins, num): 
    '''
    @coins: 所有可用的面额
    @num：最后需要凑成的金额数
    求解最少需要多少金币，才能凑成num值
    '''
    dp = [num+1]*(num+1)
    for x in range(num+1):
        for y in coins:
            if x-y<0:
                continue
            dp[x] = min(dp[x], 1+dp[x-y])
    return dp[num] if dp[num]!=num+1 else -1

if __name__ == "__main__":
    # coins = [3, 5, 2, 1, 4, 7]
    # # dp1 = [[-2]*11 for i in range(len(coins)+1)]
    # # res = coinAdd2(coins, 0, 10, dp1)
    # res = coinAdd3(coins, 10)
    # print(res)
    coins = [2,5]
    res = coinAdd5(coins, 3)
    print(res)
