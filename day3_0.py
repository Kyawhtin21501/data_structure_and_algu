def max(data):
    max = data[0]
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
    return print(max)

def binary_search(data, target):
    left = 0
    right = len(data) -1
    while left <= right:
        mid  = (left + right) // 2
        if data[mid] == target:
            return print(mid)
        elif data[mid] < target:
            left = mid + 1
            return print(left)
        else:
            right = mid - 1
            return print(right)
    return -1   

input = [int(i) for i in input().split()]
print("Please input int data :" + str(input))
max(input)
binary_search(input, 5)

