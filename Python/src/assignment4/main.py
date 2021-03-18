import random
import os
import util.benchmark

class UF_Analysis:

    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def try_connect(self, pc: bool, n: int):
        t1 = 1
        #t1 = random.randint(0, n)
        t2 = random.randint(0, n)
        self.union(t1, t2, pc)
        print(f't1: {t1} | t2: {t2}', sep=',')
        with open('aaa.csv', mode='a') as f:
            print(t1, t2, file=f, sep=',')

    #after pathcompression
    def pcfind(self, root):
        if self.parent[root] != self.parent[self.parent[root]]:
            self.parent[root] = self.pcfind(self.parent[root])
        return self.parent[root]
    #no pathcompression
    def find(self, root):
        while root != self.parent[root]:
            root = self.parent[root]
        return root

    def union(self, a, b, pc):
        if pc:
            a_root = self.pcfind(a)
            b_root = self.pcfind(b)
        else:
            a_root = self.find(a)
            b_root = self.find(b)

        if self.rank[a_root] == self.rank[b_root]:
            self.parent[a_root] = b_root
            self.rank[a_root] += 1
        elif self.rank[a_root] > self.rank[b_root]:
            self.parent[b_root] = a_root
        else:
            self.parent[a_root] = b_root


def main() -> None:
    # n = int(input("input:"))  # n determine the number of "sites"
    os.unlink('aaa.csv')
    # n = int(input("input:"))
    n = 10
    a = UF_Analysis(n)
    pc = True
    for _ in range(1000000):
        a.try_connect(pc, n)
        #  print("n", n)
    #  print('{}'.format(n), file=f)


if __name__ == '__main__':
    main()
