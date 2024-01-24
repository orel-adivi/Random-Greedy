#
#   @file : Code.py
#   @date : 24 January 2024
#   @authors : Orel Adivi and Daniel Noor
#
import numpy as np
import pylcs
from abc import ABC, abstractmethod

from utils.LevenshteinDistance import levenshtein_deletion_distance


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

    def max_deletions_old(self) -> int:
        sorted_words = sorted(self.codewords, key=lambda x: x.count('1'))
        max_lcs = 0
        sorted_counts = [x.count('1') for x in sorted_words]
        for i, w1 in enumerate(sorted_words):
            for j, w2 in enumerate(sorted_words[0:i]):
                if min(sorted_counts[i], sorted_counts[j]) \
                        + min(self.length - sorted_counts[i], self.length - sorted_counts[j]) <= max_lcs:
                    continue
                lcs = pylcs.lcs_sequence_length(w1, w2)
                if lcs > max_lcs:
                    max_lcs = lcs
        return self.length - max_lcs - 1

    def max_deletions(self) -> int:
        sorted_words = sorted(self.codewords, key=lambda x: x.count('1'))
        max_lcs = 0
        sorted_counts = [x.count('1') for x in sorted_words]
        for i, w1 in enumerate(sorted_words):
            for j, w2 in enumerate(sorted_words[0:i]):
                if min(sorted_counts[i], sorted_counts[j]) \
                        + min(self.length - sorted_counts[i], self.length - sorted_counts[j]) <= max_lcs:
                    break
                lcs = pylcs.lcs_sequence_length(w1, w2)
                if lcs > max_lcs:
                    max_lcs = lcs
            for j, w2 in enumerate(sorted_words[i-1:-1:-1]):
                if min(sorted_counts[i], sorted_counts[j]) \
                        + min(self.length - sorted_counts[i], self.length - sorted_counts[j]) <= max_lcs:
                    break
                lcs = pylcs.lcs_sequence_length(w1, w2)
                if lcs > max_lcs:
                    max_lcs = lcs
        return self.length - max_lcs - 1
