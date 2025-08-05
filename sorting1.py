def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]      # 今の値
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 右にずらす
            j -= 1
        arr[j + 1] = key  # 正しい場所に挿入
    return arr

print(insertion_sort([3,5,6,2,5,6,7,9,8]))