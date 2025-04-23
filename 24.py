n = int(input())
a = list(map(int, input().split()))
mx = max(a)
sm= sum(a) - mx
if sm >= mx:
    print(sm + mx)
else:
    print(sm * 2 + 1)