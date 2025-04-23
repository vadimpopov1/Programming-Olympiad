k = int(input())

for _ in range(k):
    s = input()
    flag = 0
    pairs = 0
    if flag == 0:
        for i in range(len(s)):
            if s[i] == '(':
                for j in range(i + 1, len(s)):
                    if s[j] == ')':
                        while s[j] == ')':
                            s = s.replace(')', '1', 1)
                        pairs += 1
                        flag = 1
                        break
            if s[i] == '[':
                for j in range(i + 1, len(s)):
                    if s[j] == ']':
                        while s[j] == ']':
                            s = s.replace(']', '1', 1)
                        pairs += 1
                        flag = 1
                        break
        print(pairs)
    else:
        print(0)