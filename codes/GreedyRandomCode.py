#
#   @file : GreedyRandomCode.py
#   @date : 2 March 2023
#   @authors : Orel Adivi and Daniel Noor
#
from overrides import overrides
import numpy as np

from codes.Code import Code
from utils.LongestCommonSubsequence import longest_common_subsequence


class GreedyRandomCode(Code):
    @overrides
    def __init__(self, length=20, options=2):
        words = int(np.ceil(np.log2(length)))
        self.options = options
        super().__init__(length, words)
        self._insert_codeword(0, '0' * self.length)
        self._insert_codeword(1, '1' * self.length)
        for i in range(2, words):
            candidates = [np.random.choice([0, 1], size=length) for _ in range(self.options)]
            for j in range(options):
                while Code._codeword_as_str(candidates[j]) in self.codewords:
                    candidates[j] = np.random.choice([0, 1], size=length)
            dists = [max([longest_common_subsequence(candidates[j], c) for c in self.codewords])
                     for j in range(options)]
            self._insert_codeword(i, Code._codeword_as_str(candidates[dists.index(min(dists))]))


if __name__ == "__main__":
    r = GreedyRandomCode(100)
    print(r.codewords)
    print(r.max_deletions())
    print(r.decode(r.mapping[3][0:80]))
