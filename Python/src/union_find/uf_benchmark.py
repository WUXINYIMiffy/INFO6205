from util.benchmark import Benchmark
from union_find.uf_hwqupc import UF_HWQUPC


class Test_UF_HWQUPC(UF_HWQUPC):

    def do_path_compression_all_to_root_test(self, p_r: tuple):
        return self.do_path_compression_all_to_root(*p_r)


def main():

    hw = Test_UF_HWQUPC(2000)

    bm = Benchmark(hw.do_path_compression)
    x = bm.run(1000, 10000)
    print(f"do_path_compression: {x} millisecs")

    bm = Benchmark(hw.do_path_compression_all_to_root_test)
    x = bm.run((1000, 1000), 10000)
    print(f"path_compression_all_to_root: {x} millisecs")


if __name__ == '__main__':
    main()
