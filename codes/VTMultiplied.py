#
#   @file : VTMultiplied.py
#   @date : 19 March 2023
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np
from utils import vt

from codes.Code import Code


class VTMultiplied(Code):
    @overrides
    def __init__(self, length=20, m=5):
        words = length
        super().__init__(length, words)
        self.width = m
        vt_code = vt.VTCode(self.width, 2)
        count = min(np.power(2, vt_code.k), words)
        for i in range(count):
            codeword = np.array(list(np.binary_repr(i).zfill(vt_code.k))).astype(np.int8)
            codeword = vt_code.encode(codeword)
            self._insert_codeword(i, self.__multiply(codeword))

    def __multiply(self, codeword):
        return ''.join([str(x) * int(np.ceil(self.length / self.width))
                        for x in codeword])[0:self.length]


if __name__ == "__main__":
    l = 2000
    log_l = int(np.ceil(np.log2(l)))
    m = log_l + int(np.ceil(np.log2(log_l))) + 1
    r = VTMultiplied(l, m)
    print(len(r.codewords))
    print(r.max_deletions())

