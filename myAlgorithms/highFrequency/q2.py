'''
Descripttion: 归并排序
Author: lishaogang
version: 
Date: 2021-12-25 08:42:04
LastEditors: lishaogang
LastEditTime: 2021-12-25 09:50:47
'''

def merge(arr, l1, mid, r2):
    res = []
    i, j = l1, mid+1
    while i<=mid and j<=r2:
        if arr[i]<=arr[j]:
            res.append(arr[i])
            i+=1
        else:
            res.append(arr[j])
            j+=1
    if i<=mid:
        res+=arr[i:mid+1]
    if j<=r2:
        res+=arr[j:r2+1]
    arr[l1:r2+1] = res

def mergeSort(arr, left, right):
    if right<=left:
        return
    
    mid = left+(right-left)//2
    mergeSort(arr, left, mid)
    mergeSort(arr, mid+1, right)
    merge(arr, left, mid, right)


if __name__ == "__main__":
    import random
    arr = [random.randint(1,30) for i in range(30)]
    print(arr)
    mergeSort(arr, 0, 29)
    print(arr)