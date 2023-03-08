#
#   @file : RandomCode.py
#   @date : 8 March 2023
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np

from codes.Code import Code


class RandomCode(Code):
    @overrides
    def __init__(self, length=20):
        words = length
        super().__init__(length, words)
        for i in range(0, words):
            codeword = self.__multiply(np.random.choice([0, 1], size=int(np.ceil(np.log2(length)))))
            while Code._codeword_as_str(codeword) in self.codewords:
                codeword = self.__multiply(np.random.choice([0, 1], size=int(np.ceil(np.log2(length)))))
            self._insert_codeword(i, Code._codeword_as_str(codeword))

    def __multiply(self, codeword):
        if self.length // int(np.ceil(np.log2(self.length))) == self.length / int(np.ceil(np.log2(self.length))):
            return ''.join([str(x) * (self.length // int(np.ceil(np.log2(self.length)))) for x in codeword])
        else:
            return ''.join([str(x) * (self.length // int(np.ceil(np.log2(self.length))) + 1)
                            for x in codeword])[0:self.length]


if __name__ == "__main__":
    r = RandomCode(128)
    print(r.codewords)
    print(r.max_deletions())
    print(r.decode(r.mapping[3][0:80]))
