#
#   @file : VTRepetitionCode.py
#   @date : 05 March 2024
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np
from utils import VTCode

from codes.Code import Code


class VTRepetitionCode(Code):
    @overrides
    def __init__(self, length=20, m=5):
        words = length
        super().__init__(length, words)
        self.width = m
        vt_code = VTCode.VTCode(self.width, 2)
        count = min(np.power(2, vt_code.k), words)
        for i in range(count):
            codeword = np.array(list(np.binary_repr(i).zfill(vt_code.k))).astype(np.int8)
            codeword = vt_code.encode(codeword)
            self._insert_codeword(i, self.__multiply(codeword))

    def __multiply(self, codeword):
        return ''.join([str(x) * int(np.ceil(self.length / self.width))
                        for x in codeword])[0:self.length]
