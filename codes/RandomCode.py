#
#   @file : RandomCode.py
#   @date : 28 February 2023
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np

from codes.Code import Code


class RandomCode(Code):
    @overrides
    def __init__(self, length=20):
        words = int(np.ceil(np.log2(length)))
        super().__init__(length, words)
        for i in range(0, words):
            codeword = np.random.choice([0, 1], size=length)
            while Code._codeword_as_str(codeword) in self.codewords:
                codeword = np.random.choice([0, 1], size=length)

            self._insert_codeword(i, Code._codeword_as_str(codeword))


if __name__ == "__main__":
    r = RandomCode(100)
    print(r.codewords)
    print(r.max_deletions())
    print(r.decode(r.mapping[3][0:80]))
