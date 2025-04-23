def isqrt(n):
    if n == 0:
        return 0
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            left = mid + 1
        else:
            right = mid - 1
    return right

def max_kegels(c):
    if c < 6:
        return 0
    s = 8 * c + 1
    sqrt_s = isqrt(s)
    n = (sqrt_s - 1) // 2
    sum_tri = n * (n + 1) // 2
    return sum_tri if sum_tri >= 6 else 0

k = int(input())
for _ in range(k):
    c = int(input())
    print(max_kegels(c))