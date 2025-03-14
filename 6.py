n = int(input())
for _ in range(n):
    t = int(input())
    a = list(map(int, input().split()))
    a1 = a.count(1)
    a2 = a.count(2)
    if (a1 + a2 * 2 ) % 2 != 0:
        print("NO")
    else:
        h = (a1 + a2 * 2 ) // 2
        if h % 2 == 0:
            print("YES")
        else:
            if a1 >= 1:
                print("YES")
            else:
                print("NO")