from union_find.uf_hwqupc import UF_HWQUPC
import random


def uf_main():
    n = int(input("input:"))  # n determine the number of "sites"
    t1 = random.randint(0, n - 1)
    t2 = random.randint(0, n - 1)
    print(t1, t2)

    h = UF_HWQUPC(n)


if __name__ == '__main__':
    uf_main()
