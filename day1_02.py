n = int(input())
a = [int(input()) for _ in range(n)]
k = int(input())

num_k = []
for i, num in enumerate(a):
    if num == k:
        num_k.append(i)

if num_k:
    print(num_k[0], num_k[-1])
else:
    print(-1, -1)
