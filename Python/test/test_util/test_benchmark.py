import unittest

from util.benchmark import Benchmark
from typing import List, Callable
from sort.simple.insertion_sort import InsertionSort
from random import Random


class TestBenchmark(unittest.TestCase):

    def test_full_random(self) -> None:
        def fn_xs(n: int) -> List[int]:
            random = Random()
            xs = [random.randint(0, int(1e5)) for _ in range(n)]
            return xs

        gen_data(fn_xs, 'data_full_random')

    def test_ordered(self) -> None:
        def fn_xs(n: int) -> List[int]:
            xs = list(range(n))
            return xs

        gen_data(fn_xs, 'data_ordered')

    def test_reverse_ordered(self) -> None:
        def fn_xs(n: int) -> List[int]:
            xs = list(range(n))
            xs.reverse()
            return xs

        gen_data(fn_xs, 'data_reverse_ordered')

    def test_partial_ordered(self) -> None:
        def fn_xs(n: int) -> List[int]:
            xs_1 = list(range(n // 2))
            random = Random()
            xs_2 = [random.randint(0, int(1e5)) for _ in range(n - n // 2)]
            xs = xs_1 + xs_2
            return xs

        gen_data(fn_xs, 'data_partial_ordered')


def gen_data(fn_xs: Callable[[int], List[int]], file_name: str) -> None:
    m = 50
    data_pair = []
    for n in range(0, 1001, 10):
        tot = 0
        for k in range(5):
            xs = fn_xs(n)
            tot += Benchmark.benchmark_sort(xs, f"InsertionSort: {n}", InsertionSort(), m)
        t = tot / 5
        data_pair.append((n, t))
    with open(f'{file_name}.txt', mode='w') as f:
        for n, t in data_pair:
            print(n, t, file=f)


if __name__ == "__main__":
    unittest.main()
