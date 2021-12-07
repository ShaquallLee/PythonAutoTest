'''
Descripttion: 有一个由正整数组成数组，每次只能拿最左边的数或最右边的数，
    两个人交替拿数，求先手的和后手的谁会赢
Author: lishaogang
version: 
Date: 2021-12-07 08:38:14
LastEditors: lishaogang
LastEditTime: 2021-12-07 09:11:06
'''


def numberGet(arr):
    def f(arr, l, r):
        '''
        先手的操作'''
        if l == r:
            return arr[l]
        return max(
            arr[l]+s(arr, l+1, r),
            arr[r]+s(arr, l, r-1)
        )

    def s(arr, l, r):
        '''
        后手的操作'''
        if l == r:
            return 0
        # 因为是后手，所以先手会先选择他算出来的值会比较大的数，剩给后手的相比较小的情况（故用min）
        # 后手只能从剩下的这些数中作为先手去选择对它最有利的选择（故使用f函数）。
        return min(
            f(arr, l+1, r),
            f(arr, l, r-1)
        )
    return max(f(arr, 0, len(arr)-1), s(arr, 0, len(arr)-1))


def numberGet2(arr):
    '''
    使用动态规划来解决这个问题'''
    l = len(arr)
    f = [[-1]*l for i in range(l)]  # f表示先手拿到的最好结果，
    # 如第i行第j列的值表示从第i个数开始到第j个数，作为先手能够拿到的最高的分

    s = [[-1]*l for i in range(l)]  # s表示后手拿到的最后的结果，
    # 如第i行第j列的值表示的是从第i个数开始到第j个数，作为后手能够拿到的最高分

    for i in range(l):
        f[i][i] = arr[i]
        s[i][i] = 0

    for j in range(1, l):
        x = 0
        y = j
        while y < l:
            f[x][y] = max(
                arr[x]+s[x+1][y],
                arr[y]+s[x][y-1]
            )
            s[x][y] = min(
                f[x+1][y],
                f[x][y-1]
            )
            x += 1
            y += 1
    return "先手赢" if f[0][l-1]>s[0][l-1] else "后手赢" #这样求到的是谁能赢
    # return max(f[0][l-1], s[0][l-1])    #这样求到的是两人中能够拿到的最高分


if __name__ == "__main__":
    arr = [1, 100, 30, 50, 20]
    # res = numberGet(arr)
    res = numberGet2(arr)
    print(res)
