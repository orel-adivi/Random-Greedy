#
#   @file : VTRepetitionNaryCode.py
#   @date : 14 April 2024
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np
from utils import VTCode

from codes.Code import Code


class VTRepetitionNaryCode(Code):
    """This code takes all words from VT0(m, q) for some m and q. First we convert
     each codeword to binary and then multiply each letter n/m times (n is the code length).
    The parameter m is chosen to get a code with slightly more than n codewords, and redundant
    words are removed."""

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
