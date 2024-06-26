#
#   @file : RepetitionCode.py
#   @date : 13 April 2024
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np

from codes.Code import Code


class RepetitionCode(Code):
    """This code generates all words of length log(n) and multiplies each letter
    n/log(n) times, giving words of length n."""

    @overrides
    def __init__(self, length=20):
        words = length
        super().__init__(length, words)
        width = int(np.ceil(np.log2(self.length)))
        for i in range(0, words):
            codeword = self.__multiply(np.binary_repr(i, width=width))
            self._insert_codeword(i, codeword)

    def __multiply(self, codeword):
        return ''.join([str(x) * int(np.ceil(self.length / int(np.ceil(np.log2(self.length)))))
                        for x in codeword])[0:self.length]
