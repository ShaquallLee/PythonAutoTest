'''
Descripttion: 解决机器人运动问题
参数N：有N个可移动的位置
参数S：机器人开始的位置
参数e：机器人移动的目标终点位置
参数k：机器人通过走k步到达终点e
求：机器人从s位置开始通过走k步到终点位置e的方法的个数
每次只能向左或向右移动一步
Author: lishaogang
version: 
Date: 2021-12-06 10:27:05
LastEditors: lishaogang
LastEditTime: 2021-12-06 17:24:00
'''

def robotMove(N, E, rest, p):
    '''
    discription:递归形式解决机器人运行问题
    params:
        N:位置的个数
        E：终点的位置
        rest：当前剩余可走的步数
        p：当前的位置
    return：
        从起点走到终点的方式的种数
    '''
    if rest == 0:
        return 1 if p==E else 0
    if p==1:
        return robotMove(N, E, rest-1, 2)
    if p==N:
        return robotMove(N, E, rest-1, p-1)
    return robotMove(N, E, rest-1, p+1) + robotMove(N, E, rest-1, p-1)


def robotMove2(N, E, rest, p, dp):
    '''
    相比于1代，添加了dp用来存储已经算过的信息，避免二次计算'''
    if dp[rest][p]!=-1:
        return dp[rest][p]
    if rest==0:
        dp[rest][p] = 1 if p==E else 0
        return dp[rest][p]
    if p==1:
        dp[rest][p] = robotMove2(N, E, rest-1, 2, dp)
        return dp[rest][p]
    if p==N:
        dp[rest][p] = robotMove2(N, E, rest-1, p-1, dp)
        return dp[rest][p]
    dp[rest][p] = robotMove2(N, E, rest-1, p-1, dp) + robotMove2(N, E, rest-1, p+1, dp)
    return dp[rest][p]

def robotMove3(N, E, step, S):
    '''
    使用状态转移方程的方式计算
    将上面两种解法的3个递归条件转化到这个算法中
    params：
        N：位置数
        E：结束位置
        step：规定的走多少步
        S：开始的位置
    others：
        状态转移方程dp2
        dp2中行为步数，列为位置，第i行第j列的值代表的是从第j位置开始走i步能够到达终点的走法个数
        如：最后一行表示的是从各个位置开始，能够到达终点的走法的个数
    '''
    dp2 = [[0]*N for i in range(step+1)]
    dp2[0][E-1]=1
    for i in range(1, step+1):
        for j in range(N):
            if j==0:
                dp2[i][j]=dp2[i-1][j+1]
            elif j==N-1:
                dp2[i][j]=dp2[i-1][j-1]
            else:
                dp2[i][j]=dp2[i-1][j-1]+dp2[i-1][j+1]
    return dp2[step][S-1]

if __name__ == "__main__":
    dp = [[-1]*6 for i in range(5)]
    # res = robotMove2(5, 4, 4, 2, dp)
    # res = robotMove(5, 4, 4, 2)
    res = robotMove3(5, 4, 4, 2)
    print(res)