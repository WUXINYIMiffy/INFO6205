from union_find.uf_hwqupc import UF_HWQUPC
import random


class UF_Analysis:
    @staticmethod
    def count(n: int) -> int:
        m = 0

        h = UF_HWQUPC(n)
        while h.count != 1:
            m += try_connect(h, n)

        return m


def try_connect(h: UF_HWQUPC, n: int) -> int:
    t1 = random.randint(0, n - 1)
    t2 = random.randint(0, n - 1)
    dm = 1
    if not h.connected(t1, t2):
        h.union(t1, t2)
    return dm


def main() -> None:
    # n = int(input("input:"))  # n determine the number of "sites"
    with open('stats.csv', 'w') as f:
        for n in range(1, 1000000):
            m = 0
            for _ in range(50):
                m += UF_Analysis.count(n)
            m = m / 50
            print("n", n, "m", m)
            print('{},{}'.format(n, m), file=f)


if __name__ == '__main__':
    main()
