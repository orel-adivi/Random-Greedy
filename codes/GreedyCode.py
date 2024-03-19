#
#   @file : GreedyCode.py
#   @date : 05 March 2024
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np

from codes.Code import Code


"""A code generator which generates codewords one by one. 
With each generation we try creating a codeword which is as different as
possible from all previously generated codeword."""
class GreedyCode(Code):
    @overrides
    def __init__(self, length=20):
        words = length
        super().__init__(length, words)
        self._insert_codeword(0, '0' * self.length)
        for i in range(1, words):
            codeword = self.__generate_next()
            while codeword in self.codewords:
                codeword = self.__generate_next()
            self._insert_codeword(i, codeword)

    # start with the all-0 codeword, then go over existing codewords and tweak it until
    # it's "different enough" from them
    def __generate_next(self):
        next_codeword = '0' * self.length
        for codeword in self.codewords:
            next_codeword = "".join(
                [str(1 - int(codeword[i])) if codeword[i] == next_codeword[i]
                 else Code._codeword_as_str(np.random.choice([0, 1], size=1)) for i in range(self.length)]
            )
        return next_codeword
