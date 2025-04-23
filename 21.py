a = int(input())
b = int(input())
c = int(input())
if a == 0 or b == 0 or c == 0:
    print(0)
else:
    print(min(a, b // 2, c // 4) * 7)