#
#   @file : LevenshteinDistance.py
#   @date : 05 March 2024
#   @authors : Orel Adivi and Daniel Noor
#
import numpy as np


"""Computes Levenshtein deletion distance between an expected string and the measured/received string."""
def levenshtein_deletion_distance(expected: str, measured: str):
    dims = (len(measured) + 1, len(expected) + 1)
    dp_matrix = np.zeros(dims, dtype=np.int64)
    for index_expected in range(1, dims[1]):  # init first row
        dp_matrix[0][index_expected] = index_expected
    for index_actual in range(1, dims[0]):  # init first column
        dp_matrix[index_actual][0] = index_actual
    for index_actual in range(1, dims[0]):
        for index_expected in range(1, dims[1]):
            if measured[index_actual - 1] == expected[index_expected - 1]:
                dp_matrix[index_actual][index_expected] = dp_matrix[index_actual - 1][index_expected - 1]
            else:
                dp_matrix[index_actual][index_expected] = 1 + min(dp_matrix[index_actual][index_expected - 1],
                                                                  dp_matrix[index_actual - 1][index_expected])
    return dp_matrix[-1][-1]
