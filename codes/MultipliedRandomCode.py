#
#   @file : MultipliedRandomCode.py
#   @date : 8 March 2023
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np
from timeit import timeit

from codes.Code import Code


class MultipliedRandomCode(Code):
    @overrides
    def __init__(self, length=20):
        words = length
        super().__init__(length, words)
        for i in range(0, words):
            codeword = self.__multiply(np.random.choice([0, 1], size=int(np.ceil(np.log2(length)))))
            while codeword in self.codewords:
                codeword = self.__multiply(np.random.choice([0, 1], size=int(np.ceil(np.log2(length)))))
            self._insert_codeword(i, codeword)

    def __multiply(self, codeword):
        return ''.join([str(x) * int(np.ceil(self.length / int(np.ceil(np.log2(self.length)))))
                        for x in codeword])[0:self.length]
        # if self.length // int(np.ceil(np.log2(self.length))) == self.length / int(np.ceil(np.log2(self.length))):
        #     return ''.join([str(x) * (self.length // int(np.ceil(np.log2(self.length)))) for x in codeword])
        # else:
        #     return ''.join([str(x) * (self.length // int(np.ceil(np.log2(self.length))) + 1)
        #                     for x in codeword])[0:self.length]


if __name__ == "__main__":
    r = MultipliedRandomCode(200)
    # print(r.codewords)
    print(timeit(lambda: print(r.max_deletions_old()), number=1))
    print(timeit(lambda: print(r.max_deletions()), number=1))
