#
#   @file : SimpleGreedyCode.py
#   @date : 1 March 2023
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np

from codes.Code import Code


class SimpleGreedyCode(Code):
    @overrides
    def __init__(self, length=20):
        words = int(np.ceil(np.log2(length)))
        super().__init__(length, words)
        self._insert_codeword(0, '0' * self.length)
        for i in range(1, words):
            codeword = self.__generate_next()
            while codeword in self.codewords:
                codeword = self.__generate_next()
            self._insert_codeword(i, codeword)

    def __generate_next(self):
        next_codeword = '0' * self.length
        for codeword in self.codewords:
            next_codeword = "".join(
                [str(1 - int(codeword[i])) if codeword[i] == next_codeword[i]
                 else Code._codeword_as_str(np.random.choice([0, 1], size=1)) for i in range(self.length)]
            )
        return next_codeword


if __name__ == "__main__":
    r = SimpleGreedyCode(100)
    print(r.codewords)
    print(r.max_deletions())
    print(r.decode(r.mapping[3][0:80]))
