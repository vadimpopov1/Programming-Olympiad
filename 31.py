t = int(input())

for _ in range(t):
    n, m, l, r = map(int, input().split())
    
    l = max(l ,-m)
    print(l, l + m)