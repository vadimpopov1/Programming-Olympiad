n = int(input())
if n < 1 or n > 5000:
    print("Error! Value will be more then 1 and less the 5.000!")
y = list(map(int, input().split()))
list_prog = []
list_math = []
list_phy = []
for i in range(n):
    if y[i] == 1:
        list_prog.append(i+1)
    if y[i] == 2:
        list_math.append(i+1)
    if y[i] == 3:
        list_phy.append(i+1)
m = min(len(list_prog), len(list_math), len(list_phy))
print(m)
for i in range(m):
    print(list_prog[i], list_math[i], list_phy[i])