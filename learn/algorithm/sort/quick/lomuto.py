import random


def quick_sort(arr, l_idx, r_idx):
    """快速排序——单路快速排序(lomuto 洛穆托分区方案) 递归版
    1. 选择最右元素作为基准点元素
    2. j指针负责找到比基准点小的元素, 一旦找到则与i进行交换
    3. i指针维护小于基准点元素的边界, 也是每次交换的目标索引
    4. 最后基准点与i元素交换, i即为分区位置
    5. 分治(递归): 对以上分出的左右区间重复 直到各区间只有⼀个数
        在 quick_sort(array, 0, len(array) - 1) 中调用:
        quick_sort(array, l_idx, pivot - 1) 和 quick_sort(array, pivot + 1, r_idx)

    Arguments:
        array {[array]} -- 待排序数组
        l_idx {[int]} -- 左区间index
        r_idx {[int]} -- 右区间index

    Returns:
        [None] -- None
    """
    if l_idx >= r_idx:
        return

    # 选择最左值的位置作为基准点索引 pivot_idx, 选择最右值作为基准点值 pivot_val
    pivot_idx, pivot_val = l_idx, arr[r_idx]
    # print(f'BEFORE_LOOP: l_idx: {l_idx}, r_idx: {r_idx}, pivot_idx: {pivot_idx}, pivot_val: {pivot_val}, arr: {arr}')

    # 为 pivot_val 找到其应有的位置: 遍历区间 [l_idx, r_idx] 找到比 pivot_val 小的值 并与 pivot_idx 交换
    for idx, val in enumerate(arr[l_idx:r_idx]):
        if val <= pivot_val:
            arr[pivot_idx], arr[idx + l_idx] = arr[idx + l_idx], arr[pivot_idx]
            pivot_idx += 1

    # 一趟过后: 此时 pivot_idx 已经是 pivot_val 应有的排序位置 左边的值都小于 pivot_val 右边的值都大于 pivot_val
    # print(f' AFTER_LOOP: l_idx: {l_idx}, r_idx: {r_idx}, pivot_idx: {pivot_idx}, pivot_val: {pivot_val}, arr: {arr}')
    # 交换值的位置: 将 pivot_val 放在 pivot_idx 位置
    arr[pivot_idx], arr[r_idx] = arr[r_idx], arr[pivot_idx]

    quick_sort(arr, l_idx, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, r_idx)


# def lomuto_partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1


# def quick_sort(arr, low, high):
#     if low < high:
#         pi = lomuto_partition(arr, low, high)
#         quick_sort(arr, low, pi - 1)
#         quick_sort(arr, pi + 1, high)


if __name__ == '__main__':
    array = [i for i in range(0, 19)]
    random.shuffle(array)
    array = [5, 1, 3, 4, 0, 2]
    print(len(array), array)
    quick_sort(array, 0, len(array) - 1)
    print(array)
    '''Output:
    6 [5, 1, 3, 4, 0, 2]
    BEFORE_LOOP: l_idx: 0, r_idx: 5, pivot_idx: 0, pivot_val: 2, arr: [5, 1, 3, 4, 0, 2]
    AFTER_LOOP: l_idx: 0, r_idx: 5, pivot_idx: 2, pivot_val: 2, arr: [1, 0, 3, 4, 5, 2]
    BEFORE_LOOP: l_idx: 0, r_idx: 1, pivot_idx: 0, pivot_val: 0, arr: [1, 0, 2, 4, 5, 3]
    AFTER_LOOP: l_idx: 0, r_idx: 1, pivot_idx: 0, pivot_val: 0, arr: [1, 0, 2, 4, 5, 3]
    BEFORE_LOOP: l_idx: 3, r_idx: 5, pivot_idx: 3, pivot_val: 3, arr: [0, 1, 2, 4, 5, 3]
    AFTER_LOOP: l_idx: 3, r_idx: 5, pivot_idx: 3, pivot_val: 3, arr: [0, 1, 2, 4, 5, 3]
    BEFORE_LOOP: l_idx: 4, r_idx: 5, pivot_idx: 4, pivot_val: 4, arr: [0, 1, 2, 3, 5, 4]
    AFTER_LOOP: l_idx: 4, r_idx: 5, pivot_idx: 4, pivot_val: 4, arr: [0, 1, 2, 3, 5, 4]
    [0, 1, 2, 3, 4, 5]
    '''
