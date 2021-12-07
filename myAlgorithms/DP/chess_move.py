'''
Descripttion: 象棋的棋盘是9*10的，有个马在任意位置，让它跳step步到达某个点
    求跳的方法的个数，即有多少种不同的跳法能够到达终点位置
Author: lishaogang
version: 
Date: 2021-12-07 10:04:10
LastEditors: lishaogang
LastEditTime: 2021-12-07 10:35:37
'''

def chessMove(x, y, step, startx, starty):
    if step==0:
        return 1 if x==startx and starty==y else 0
    if x<0 or x>8 or y<0 or y>9:
        return 0
    
    return sum([chessMove(x+1, y+2, step-1, startx, starty),
            chessMove(x+2, y+1, step-1, startx, starty),
            chessMove(x+1, y-2, step-1, startx, starty),
            chessMove(x+2, y-1, step-1, startx, starty),
            chessMove(x-1, y+2, step-1, startx, starty),
            chessMove(x-1, y-2, step-1, startx, starty),
            chessMove(x-2, y+1, step-1, startx, starty),
            chessMove(x-2, y-1, step-1, startx, starty)])


def chessMove2(x, y, step, startx, starty):
    '''
    使用动态规划的方法'''
    dp = [[[0]*(step+1) for i in range(9)] for j in range(10)]

    dp[startx][starty][0]=1

    getN = lambda i,j, s: dp[i][j][s] if i>=0 and j>=0 and i<10 and j<9 else 0

    for stepi in range(1,step+1):
        for xi in range(10):
            for yi in range(9):
                dp[xi][yi][stepi]=sum([getN(xi+1, yi+2, stepi-1),
                                    getN(xi+2, yi+1, stepi-1),
                                    getN(xi+1, yi-2, stepi-1),
                                    getN(xi+2, yi-1, stepi-1),
                                    getN(xi-1, yi+2, stepi-1),
                                    getN(xi-1, yi-2, stepi-1),
                                    getN(xi-2, yi+1, stepi-1),
                                    getN(xi-2, yi-1, stepi-1)])
    return dp[x][y][step]

if __name__ == "__main__":
    print(chessMove2(0,2, 4, 0, 0))