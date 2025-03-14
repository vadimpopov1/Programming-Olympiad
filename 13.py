def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def s():
    n = int(input()) - 2
    a = list(map(int, input().split()))
    a = quicksort(a)
    a_set = set(a)
    for i in a_set:
        if n % i == 0 and n // i in a:
            print(i, n // i)
            return 1

k = int(input())
for _ in range(k):
    s()