'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-12-08 12:07:13
LastEditors: lishaogang
LastEditTime: 2021-12-08 12:13:36
'''

def maxSumOfThreeSubarrays(nums, k):
    nums_len = len(nums)

    dp = [[[0]*4 for j in range(nums_len)] for i in range(3)]

    for posi in range(k-1, nums_len):
        s = sum(nums[posi-k+1:posi+1])
        if s>dp[0][posi-1][0]:
            dp[0][posi][0] = s
            dp[0][posi][1] = posi-k+1
        else:
            dp[0][posi] = dp[0][posi-1][:] 

    for step in range(1, 3):
        for posi in range((step+1)*k-1, nums_len):
            s = dp[step-1][posi-k][0]+ sum(nums[posi-k+1:posi+1])
            if s>dp[step][posi-1][0]:
                dp[step][posi][0] = s
                dp[step][posi][1:] = dp[step-1][posi-k][1:]
                dp[step][posi][step+1]=posi-k+1
            else:
                dp[step][posi] = dp[step][posi-1][:]
    return dp[-1][-1][1:]
    

if __name__ == "__main__":
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    res = maxSumOfThreeSubarrays(nums, k)
    print(res)