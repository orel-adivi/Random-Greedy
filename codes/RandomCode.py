#
#   @file : RandomCode.py
#   @date : 28 February 2023
#   @authors : Orel Adivi and Daniel Noor
#
from codes.Code import Code
import numpy as np


class RandomCode(Code):
    def __init__(self, n=20):
        super().__init__(n)
        for i in range(0, int(np.ceil(np.log2(n)))):
            codeword = np.random.choice([0, 1], size=n)
            while self.arr_to_str(codeword) in self.code:
                codeword = np.random.choice([0, 1], size=n)

            self.code.append(self.arr_to_str(codeword))

    def encode(self, value: int):
        pass

    def decode(self, codeword: str):
        pass

    @staticmethod
    def arr_to_str(codeword: np.ndarray):
        return "".join([str(x) for x in codeword])


if __name__ == "__main__":
    r = RandomCode(100)
    print(r.code)
    print(r.number_of_deletions())
