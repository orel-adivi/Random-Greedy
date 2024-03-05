#
#   @file : LinSpaceCode.py
#   @date : 05 March 2024
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np

from codes.Code import Code


class LinSpaceCode(Code):
    @overrides
    def __init__(self, length=20):
        words = int(np.ceil(np.log2(length)))
        super().__init__(length, words)
        self._insert_codeword(0, '0' * self.length)
        self._insert_codeword(1, '1' * self.length)
        for i, j in zip(range(2, words), np.linspace(1, self.length/2, num=words-2)):
            codeword = (self.length * ('0' * int(j) + '1' * int(j)))[0:self.length]
            self._insert_codeword(i, codeword)
