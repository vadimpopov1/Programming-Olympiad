n = int(input())
if n < 12 or n > 1000000:
    print("Error! Value will be less then 12 and more then 1.000.000!")
if n % 2 == 0:
    x = 4
    y = (n - 4)
elif n % 2 != 0:
    x = 6
    y = (n - 6)
if x + y != n:
    print(f"Error! x + y != {n}!")
else:
    print(x, y)
