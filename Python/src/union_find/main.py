from union_find.uf_hwqupc import UF_HWQUPC
import random


def main():
    n = int(input("input:"))  # n determine the number of "sites"
    t1 = random.randint(0, n - 1)
    t2 = random.randint(0, n - 1)

    m = 0

    h = UF_HWQUPC(n)
    h1 = h.connected(t1,t2)
    while not h1:
        # t1 = random.randint(0, n - 1)
        # t2 = random.randint(0, n - 1)
        a,b = h.union(t1,t2)
        m += 1
        h1 = h.connected(a,b)

        # h1 = h.connected(t1, t2)
    print("m",m)
    print("n",n)
    print(h.count)

if __name__ == '__main__':
    main()
