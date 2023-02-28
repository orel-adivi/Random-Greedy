#
#   @file : LongestCommonSubsequence.py
#   @date : 28 February 2023
#   @authors : Orel Adivi and Daniel Noor
#
import numpy as np


def longest_common_subseq(w1: str, w2: str):
    dims = (len(w1) + 1, len(w2) + 1)
    dp_matrix = np.zeros(dims, dtype=np.int64)
    for i1 in range(1, dims[0]):
        for i2 in range(1, dims[1]):
            if w1[i1-1] == w2[i2-1]:
                dp_matrix[i1][i2] = 1 + dp_matrix[i1-1][i2-1]
            else:
                dp_matrix[i1][i2] = max(
                    dp_matrix[i1][i2-1],
                    dp_matrix[i1-1][i2]
                )
    return dp_matrix[-1][-1]


if __name__ == "__main__":
    print(longest_common_subseq("111", "000"))
    print(longest_common_subseq("10101", "10010"))
