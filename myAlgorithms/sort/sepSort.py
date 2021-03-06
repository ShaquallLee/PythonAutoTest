'''
Descripttion: 归并排序
Author: lishaogang
version: 
Date: 2021-11-15 08:35:33
LastEditors: lishaogang
LastEditTime: 2021-11-15 10:47:29
'''
ssum = 0
rsum = 0

def merge(arr, left, mid, right):
    res = []
    i,j=left, mid
    while i<mid and j<right:
        if arr[i]<=arr[j]:
            res.append(arr[i])
            i+=1
        else:
            res.append(arr[j])
            j+=1
    if i<mid:
        res+=arr[i:mid]
    if j<right:
        res+=arr[j:right]
    arr[left:right]=res

def merge4ReversedCouple(arr, left, mid, right):
    '''
    用于求解逆序对问题：
        对于一个数组中，任意i和j两个位置，且i<j,
        有arr[i]>arr[j],则称i和j位置的数是一个逆数对。
        求这个数组中共有多少个逆数对
    求解：
        也是使用归并排序的思想
        merge时，当左边的数比右边的数大时，
        说明左边数组剩余位置的元素也都比右边这个数大
        此时，rsum += 左边数组长度-左边指针当前位置
        算法运行结束后，rsum的值即为逆序对的个数
    '''
    global rsum
    res = []
    i,j=left, mid
    while i<mid and j<right:
        if arr[i]<=arr[j]:
            res.append(arr[i])
            i+=1
        else:
            res.append(arr[j])
            rsum+=mid-i
            j+=1
    if i<mid:
        res+=arr[i:mid]
    if j<right:
        res+=arr[j:right]
    arr[left:right]=res


def merge4SmallSum(arr, left, mid, right):
    '''
    用于求解小和问题：
        在一个数组中，对于第k个位置的数来说，
        位于它前面的k个数中比它小的那些数之和称为它的小和，
        求解整个数组中所有数的小和之和。
        比如：对于数组【1,3,4,2,5】，他们的小和分别为：
        1：0
        3:1
        4:1+3=4
        2:1
        5:1+3+4+2=10
        总和 = 0+1+4+1+10 = 16
    求解：
        正常情况下整个数组遍历求解其值，时间复杂度为O(n^2)
        可以使用归并排序的思想进行求解。
        在归并排序中，在其merge时，
        若左边的当前数比右边的数小，则
        ssum += 左边数的值 * 右边剩余数组的长度
        循环下来，ssum即是最终的求解
    '''
    res = []
    global ssum
    i,j=left,mid
    while i<mid and j<right:
        if arr[i]<arr[j]:
            res.append(arr[i])
            ssum+=(right-j)*arr[i] ##只需要在归并排序基础上加上这一行代码即可
            i+=1
        else:
            res.append(arr[j])
            j+=1
    if i<mid:
        res+=arr[i:mid]
    if j<right:
        res+=arr[j:right]
    arr[left:right] = res

def sepSort(arr, left, right):
    if left==right or right-left==1:
        return
    
    mid = left + ((right-left)>>1)
    sepSort(arr, left, mid)
    sepSort(arr, mid, right)
    merge4ReversedCouple(arr, left, mid, right)


if __name__ == "__main__":
    arr = [1,3,4,2,5]
    # test(arr)
    sepSort(arr, 0, len(arr))
    print(arr)
    print(rsum)