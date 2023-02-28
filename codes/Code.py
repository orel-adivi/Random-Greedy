#
#   @file : Code.py
#   @date : 28 February 2023
#   @authors : Orel Adivi and Daniel Noor
#
from abc import ABC, abstractmethod
import itertools
from utils.LongestCommonSubsequence import longest_common_subseq


class Code(ABC):
    def __init__(self, n=20):
        self.n = n
        self.code = []

    @abstractmethod
    def encode(self, value: int):
        pass

    @abstractmethod
    def decode(self, codeword: str):
        pass

    def number_of_deletions(self):
        return self.n - max([longest_common_subseq(w1, w2) for w1, w2 in itertools.combinations(self.code, 2)])
