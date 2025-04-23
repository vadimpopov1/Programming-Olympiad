s = input()
b = list(map(int, input().split()))

max_l = 0
c = [0] * 26
l = 0

for i in range(len(s)):
    id = ord(s[i]) - 97
    c[id] += 1

    while c[id] > b[id]:
        l_id = ord(s[l])  - 97
        c[l_id] -= 1
        l += 1
    max_l = max(max_l, i - l + 1)
print(max_l)