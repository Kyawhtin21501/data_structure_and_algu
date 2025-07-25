"""
問題1
整数 n と、長さ n の数列 A、整数 k が与えられます。
数列 A の中に k が何回含まれているかを出力してください。
"""
n = int(input())
a = [int(input()) for _ in range(n)]
k = int(input())
num_k = 0
for num in a:
    if num == k:
        num_k += 1
print(num_k)