#
#   @file : VTRepetitionNaryCode.py
#   @date : 24 January 2024
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np
from utils import VTCode

from codes.Code import Code


class VTRepetitionNaryCode(Code):
    @overrides
    def __init__(self, length=100, m=9, q=4):
        words = length
        super().__init__(length, words)
        self.width = m
        self.q = q
        vt_code = VTCode.VTCode(self.width, self.q)
        count = min(np.power(self.q, vt_code.k), words)
        for i in range(count):
            codeword = np.array(list(np.binary_repr(i).zfill(vt_code.k))).astype(np.int8)
            codeword = vt_code.encode(codeword)
            self._insert_codeword(i, self.__multiply(self.__to_binary(codeword)))

    def __to_binary(self, codeword):
        return ''.join([np.binary_repr(x).zfill(int(np.ceil(np.log2(self.q)))) for x in codeword])

    def __multiply(self, codeword):
        curr_len = len(codeword)
        return ''.join([str(x) * int(np.ceil(self.length / curr_len))
                        for x in codeword])[0:self.length]


if __name__ == "__main__":
    l = 400
    log_l = int(np.ceil(np.log2(l)))
    m = log_l + int(np.ceil(np.log2(log_l))) + 1
    r = VTRepetitionNaryCode(l, m)
    print(len(r.codewords))
    print(r.max_deletions())

