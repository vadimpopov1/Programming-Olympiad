n = int(input())

for _ in range(n):
    t = int(input())
    cnt_min = 10**10
    for i in range(len(str(t))):
        temp = t
        cnt = 0
        while str(temp).count('7') == 0:
            temp += int("9" * (i+1))
            cnt += 1
        cnt_min = min(cnt, cnt_min)
        if cnt_min == 0:
            break
        if cnt_min == 1:
            break
    print(cnt_min)