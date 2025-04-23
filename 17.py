k = int(input())
cnt = 0
for _ in range(k):
    cnt += 1
    x, n, m = map(int, input().split())
    if n + m <= 10**9:
        if x == 0:
            print(0, 0)
        else:
            s1 = x
            if n > x and x % 2 == 0:
                s1 = 0
            elif n > x and x % 2 != 0:
                s1 = 1
            else:
                for i in range(n):
                    s1 = s1 // 2
                for i in range(m):
                    s1 = (s1 + 1) // 2

            s2 = x
            if m > x and x % 2 == 0:
                s2 = 0
            elif m > x and x % 2 != 0:
                s2 = 1
            else:
                for i in range(n):
                    s2 = (s2 + 1) // 2
                for i in range(m):
                    s2 = s2 // 2
            if n == 0 or m == 0 and (m != n):
                print(max(s1, s2), max(s1, s2))
            else:
                print(min(s1,s2), max(s1,s2))
    else:
        print(0,0)