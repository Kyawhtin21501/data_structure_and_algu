"""
レベル2：出現位置をすべて出力

問題2：
整数 n と、長さ n の数列 A、整数 k が与えられます。
A の中で k が出現する**すべてのインデックス（0始まり）**を、昇順に空白区切りで出力してください。
ただし、k が一度も出現しない場合は -1 を出力してください。
"""
n = int(input())
a = list(int(input()) for _ in range(n))
k = int(input())
num_k = []
for i,num in enumerate(a):
    if k == num:
        num_k.append(i)

if num_k:
    for value in num_k:
        print(value, end=" ")
else:
    print(-1)