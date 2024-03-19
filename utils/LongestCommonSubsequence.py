#
#   @file : LongestCommonSubsequence.py
#   @date : 05 March 2024
#   @authors : Orel Adivi and Daniel Noor
#
import numpy as np


"""A version of LCS we implemented before switching to an existing library."""
def longest_common_subsequence(w1: str, w2: str):
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
