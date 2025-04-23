n = int(input())
a = list(map(int, input().split()))
mx = max(a)
for i in range(n):
    a[i] = int((a[i] * 100 / mx) // 1)
print(*a, sep=' ')