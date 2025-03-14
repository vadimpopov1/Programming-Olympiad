k = int(input())
for _ in range(k):
    n, m = map(int, input().split())
    mat = [input() for i in range(n)]

    m_max = 0
    m_str = 0
    for i in range(len(mat)):
        if mat[i].count('#') > m_max:
            m_max = mat[i].count('#')
            m_str = i
    print(m_str + 1, mat[m_str].index('#') + m_max // 2 + 1)