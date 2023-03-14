#
#   @file : RandomCode.py
#   @date : 28 February 2023
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np
from timeit import timeit

from codes.Code import Code


class RandomCode(Code):
    @overrides
    def __init__(self, length=20):
        # words = int(np.ceil(np.log2(length)))
        words = length
        super().__init__(length, words)
        for i in range(0, words):
            codeword = np.random.choice([0, 1], size=length)
            while Code._codeword_as_str(codeword) in self.codewords:
                codeword = np.random.choice([0, 1], size=length)
            self._insert_codeword(i, Code._codeword_as_str(codeword))


if __name__ == "__main__":
    r = RandomCode(200)
    # print(r.codewords)
    print(timeit(lambda: print(r.max_deletions()), number=1))
    print(timeit(lambda: print(r.max_deletions_old()), number=1))
