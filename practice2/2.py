n, k = map(int, input().split())
if n < 1 or n > 2000 or k < 1 or k > 5:
    print("Error! Value n will be less then 2.000 and more then 1! \n Error! Value k will be less then 5 and more then 1!")
y = list(map(int, input().split()))
if len(y) != n:
    print("Error! Values in list more then n!")
else:
    cnt = 0
    for i in y:
        if i + k <= 5:
            cnt += 1
    print(cnt // 3)