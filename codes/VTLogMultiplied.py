#
#   @file : VTLogMultiplied.py
#   @date : 8 March 2023
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np
from utils import vt

from codes.Code import Code


class VTLogMultiplied(Code):
    @overrides
    def __init__(self, length=20):
        words = length
        super().__init__(length, words)
        width = int(np.ceil(np.log2(self.length)))
        vt_code = vt.VTCode(width, 2)
        for i in range(np.power(2, vt_code.k)):
            codeword = np.array(list(np.binary_repr(i).zfill(vt_code.k))).astype(np.int8)
            codeword = vt_code.encode(codeword)
            self._insert_codeword(i, self.__multiply(codeword))

    def __multiply(self, codeword):
        return ''.join([str(x) * int(np.ceil(self.length / int(np.ceil(np.log2(self.length)))))
                        for x in codeword])[0:self.length]


if __name__ == "__main__":
    r = VTLogMultiplied(1000)
    print(len(r.codewords))
    print(r.max_deletions())
