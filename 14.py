def s():
    n,m = map(int, input().split())
    dosc = [input() for i in range(n)]
    if dosc[0][0] == 'R':
        print("YES")
        return 1

    robs = []
    for i in range(n):
        for j in range(m):
            if dosc[i][j] == 'R':
                robs.append((i,j))

    for (i, j) in robs:
        s_up = i
        s_lenf = j
        for (k ,d) in robs:
            if k - s_up < 0 or d - s_lenf < 0:
                break
        else:
            print("YES")
            break
    else:
        print("NO")

k = int(input())
for _ in range(k):
    s()