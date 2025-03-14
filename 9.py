k = int(input())
for _ in range(k):
    s = ""
    for j in range(8):
        t = input().replace(" ", "").replace(".", "")
        if len(t) == 0:
            continue
        else:
            s += t
    print(s)