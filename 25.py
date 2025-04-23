class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.parity = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            orig_parent = self.parent[u]
            self.parent[u] = self.find(self.parent[u])[0]
            self.parity[u] ^= self.parity[orig_parent]
        return self.parent[u], self.parity[u]

    def union(self, u, v, required_relation):
        ru, pu = self.find(u)
        rv, pv = self.find(v)
        if ru == rv:
            return (pu ^ pv) == required_relation
        if self.rank[ru] < self.rank[rv]:
            ru, rv = rv, ru
            pu, pv = pv, pu
        self.parent[rv] = ru
        self.parity[rv] = (pu ^ pv) ^ required_relation
        if self.rank[ru] == self.rank[rv]:
            self.rank[ru] += 1
        return True


n, m = map(int, input().split())
dsu = DSU(n)
possible = True

for _ in range(m):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    required = 0 if t == 1 else 1
    if not dsu.union(x, y, required):
        possible = False

if not possible:
    print("NO")
else:
    color = [0] * n
    root_color = {}
    for u in range(n):
        root, p = dsu.find(u)
        if root not in root_color:
            root_color[root] = 0
        color[u] = (p ^ root_color[root]) + 1
    print("YES")
    print(' '.join(map(str, color)))