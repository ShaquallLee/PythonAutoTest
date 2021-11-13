import random

def quickSort(arr, left, right):
    '''
    快速排序
    :param arr: 待排序数组
    :param left: 最左边位置
    :param right: 最右边位置
    :return:
    '''
    if left < right:
        v = arr[left]
        i = left
        j = right
        while i != j:
            while i<j and v < arr[j]:
                j -= 1
            if i < j:
                arr[i] = arr[j]
                i += 1
            while i < j and v > arr[i]:
                i += 1
            if i < j:
                arr[j] = arr[i]
                j -= 1
        arr[i] = v
        quickSort(arr, left, i-1)
        quickSort(arr, i+1, right)

if __name__ == '__main__':
    arr = [random.randint(0, 100) for i in range(20)]
    print(arr)
    quickSort(arr, 0, 19)
    print(arr)