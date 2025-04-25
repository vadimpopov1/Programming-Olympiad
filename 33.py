n, m = map(int,  input().split()) # количество общежитий и количество писем
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(1, n):
    a[i] = a[i] + a[i-1]
for i in range(m):
    index = 0
    while b[i] > a[index]:
        index += 1
    if index == 0:
        print(index + 1, b[i])
    else:
        print(index + 1, b[i] - a[index-1])