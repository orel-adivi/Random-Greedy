#
#   @file : Code.py
#   @date : 28 February 2023
#   @authors : Orel Adivi and Daniel Noor
#
import numpy as np
import itertools
from abc import ABC, abstractmethod

from utils.LevenshteinDistance import levenshtein_deletion_distance
from utils.LongestCommonSubsequence import longest_common_subsequence


class Code(ABC):

    @staticmethod
    def _codeword_as_str(codeword: np.ndarray) -> str:
        return ''.join([str(x) for x in codeword])

    def _insert_codeword(self, value: int, codeword: str) -> None:
        assert 0 <= value < self.words
        assert value not in self.mapping.keys()
        assert codeword not in self.codewords
        self.codewords.add(codeword)
        self.mapping[value] = codeword

    @abstractmethod
    def __init__(self, length: int, words: int):
        self.length = length
        self.words = words
        assert 1 <= words <= length
        self.codewords = set()
        self.mapping = {}

    def encode(self, value: int) -> str:
        assert 0 <= value < self.words
        return self.mapping[value]

    def decode(self, word: str) -> int:
        assert len(word) <= self.length
        distances = [levenshtein_deletion_distance(codeword, word) for codeword in self.mapping.values()]
        return min(self.mapping.keys(), key=distances.__getitem__)

    def max_deletions(self) -> int:
        return self.length - max(map(lambda words: longest_common_subsequence(words[0], words[1]),
                                     itertools.combinations(self.codewords, 2))) - 1
