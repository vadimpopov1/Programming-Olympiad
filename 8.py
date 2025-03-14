n = int(input())
for _ in range(n):
    k = int(input())
    a = input()
    if len(a) > 0:
        while a[0] != a[-1]:
            a = a[1:-1]
            if len(a) < 1:
                break
    print(len(a))
