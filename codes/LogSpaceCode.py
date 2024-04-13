#
#   @file : LogSpaceCode.py
#   @date : 13 April 2024
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np

from codes.Code import Code


class LogSpaceCode(Code):
    """Uses the numpy.logspace function to get a different sequence length l for each codeword.
    The created codewords alternate between sequences of 0 and l-long sequences of 1."""

    @overrides
    def __init__(self, length=20, pattern_false='0', pattern_true='1'):
        words = int(np.ceil(np.log2(length)))
        super().__init__(length, words)
        for value, pattern_length in enumerate(np.logspace(0, np.log2(self.length), num=words, base=2)):
            if value == 0:
                codeword = pattern_false * self.length
            elif value == self.words - 1:
                codeword = pattern_true * self.length
            else:
                codeword = (pattern_false * int(pattern_length) + pattern_true * int(pattern_length)) * self.length
            self._insert_codeword(value, codeword[0:self.length])
