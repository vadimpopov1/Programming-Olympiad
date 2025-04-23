t = int(input())

s = list(input())

d = {   'A' : 0,
        'C' : 0,
        'G' : 0,
        'T' : 0}

for i in s:
    if i == 'A':
        d['A'] += 1
    elif i == 'C':
        d['C'] += 1
    elif i == 'G':
        d['G'] += 1
    elif i == 'T':
        d['T'] += 1

max_p = len(s) / 4
if len(s) % 4 != 0 or d['A'] < max_p or d['C'] < max_p or d['G'] < max_p or d['T'] < max_p:
    print("===")
    exit()

for i in range(len(s)):
    if s[i] == '?':
        if d['A'] < max_p:
            s[i] = 'A'
            d['A'] += 1
        elif d['C'] < max_p:
            s[i] = 'C'
            d['C'] += 1
        elif d['G'] < max_p:
            s[i] = 'G'
            d['G'] += 1
        elif d['T'] < max_p:
            s[i] = 'T'
            d['T'] += 1

print("".join(s))