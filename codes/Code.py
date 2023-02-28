from abc import ABC, abstractmethod
import itertools
from utils.LongestCommonSubseq import longest_common_subseq


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