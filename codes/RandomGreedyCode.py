#
#   @file : RandomGreedyCode.py
#   @date : 13 April 2024
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np
import pylcs

from codes.Code import Code


class RandomGreedyCode(Code):
    """In each iteration, this code generates m codeword candidates (the default m is 2)
    and selects the candidate with the largest distance from the previous codewords."""

    @overrides
    def __init__(self, length=20, options=2):
        words = length
        self.options = options
        super().__init__(length, words)
        self._insert_codeword(0, '0' * self.length)
        self._insert_codeword(1, '1' * self.length)
        for i in range(2, words):
            candidates = [np.random.choice([0, 1], size=length) for _ in range(self.options)]
            for j in range(options):
                while Code._codeword_as_str(candidates[j]) in self.codewords:
                    candidates[j] = np.random.choice([0, 1], size=length)
            dists = [max([pylcs.lcs_sequence_length(self._codeword_as_str(candidates[j]), c) for c in self.codewords])
                     for j in range(options)]
            self._insert_codeword(i, Code._codeword_as_str(candidates[dists.index(min(dists))]))
