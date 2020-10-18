class WeightedQuickUnion:
    def __init__(self, n):
        self.count = n
        self.id = [x for x in range(n)]
        self.size = [1 for x in range(n)]

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root != q_root:
            if self.size[p_root] < self.size[q_root]:
                self.id[p_root] = q_root
                self.size[q_root] += self.size[p_root]
            else:
                self.id[q_root] = p_root
                self.size[p_root] += self.size[q_root]
            self.count -= 1
