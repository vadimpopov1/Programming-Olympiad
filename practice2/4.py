n = int(input())
for _ in range(n):
    t = int(input())
    a = list(map(int, input().split()))
    even = odd = 0
    if t == 1:
        if a[0] % 2 != 0:
            even += 1
    else:
        for i in range(t):
            if (a[i] % 2 == i % 2):
                continue
            if i % 2 == 0:
                even += 1
            if i % 2 != 0:
                odd += 1
    if odd == even:
        print(odd)
    else:
        print(-1)