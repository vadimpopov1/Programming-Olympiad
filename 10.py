k = int(input())
for _ in range(k):
    cnt = 0
    m = []
    for i in range(10):
        m .append(input())
    for i in range(10):
        while True:
            ind = m[i].find("X")
            if ind == -1:
                break
            cnt += min(min(i + 1, ind + 1), min(10 - i, 10 - ind))
            m[i] = m[i].replace('X', '.', 1)
    print(cnt)
