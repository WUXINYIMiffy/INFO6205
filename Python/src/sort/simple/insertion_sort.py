from typing import List

from sort.simple.helper import Helper
from sort.simple.sort import Sort
from util.generic_type import C


class InsertionSort(Sort[C]):

    def __init__(self, helper: Helper[C] = None):
        if helper is None:
            helper = Helper[C]("InsertionSort")
        self.helper = helper

    def _sort(self, xs: List[C], _from: int, _to: int) -> None:
        # if _to is None:
        #     _to = len(xs) - 1
        if _to <= _from:
            return
        for i in range(_from, _to):
            j = i -1
            while 0 <= j < i:
                if not self.helper.less(xs[j+1], xs[j]):  # xs[j+1] >= xs[j]
                    break
                else: #if v < xs[j]:
                    # xs[j+1], xs[j] = xs[j], xs[j+1]
                    self.helper.swap(xs, lo=_from, hi=_to, i=j+1, j=j)
                    j -=1
                    continue



    def get_helper(self) -> Helper[C]:
        return self.helper
