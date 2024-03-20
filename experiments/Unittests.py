#
#   @file : Unittests.py
#   @date : 05 March 2024
#   @authors : Orel Adivi and Daniel Noor
#
import unittest
import pylcs
from utils.LevenshteinDistance import *
from utils.LongestCommonSubsequence import *


class TestLevenshteinDistance(unittest.TestCase):
    def test_equal_lengths(self):
        self.assertTrue(levenshtein_deletion_distance('', '') == 0)
        self.assertTrue(levenshtein_deletion_distance('1', '0') == 2)
        self.assertTrue(levenshtein_deletion_distance('1111', '0000') == 8)
        self.assertTrue(levenshtein_deletion_distance('100010', '110001') == 2)
        self.assertTrue(levenshtein_deletion_distance('101010', '111111') == 6)
        self.assertTrue(levenshtein_deletion_distance('100010', '110001') == 2)
        self.assertTrue(levenshtein_deletion_distance('11010', '11001') == 2)
        self.assertTrue(levenshtein_deletion_distance('0000010', '1100001') == 4)
        self.assertTrue(levenshtein_deletion_distance('0100010', '1100100') == 4)

    def test_longer_expected(self):
        self.assertTrue(levenshtein_deletion_distance('1', '') == 1)
        self.assertTrue(levenshtein_deletion_distance('111', '0') == 4)
        self.assertTrue(levenshtein_deletion_distance('1111', '1') == 3)
        self.assertTrue(levenshtein_deletion_distance('1000101', '110001') == 3)
        self.assertTrue(levenshtein_deletion_distance('101010', '1111') == 4)
        self.assertTrue(levenshtein_deletion_distance('100010', '11001') == 3)
        self.assertTrue(levenshtein_deletion_distance('11010', '1010') == 1)
        self.assertTrue(levenshtein_deletion_distance('0000010', '110001') == 5)
        self.assertTrue(levenshtein_deletion_distance('0100010', '110000') == 3)

    def test_longer_measured(self):
        self.assertTrue(levenshtein_deletion_distance('', '1') == 1)
        self.assertTrue(levenshtein_deletion_distance('0', '111') == 4)
        self.assertTrue(levenshtein_deletion_distance('1', '1111') == 3)
        self.assertTrue(levenshtein_deletion_distance('110001', '1000101') == 3)
        self.assertTrue(levenshtein_deletion_distance('1111', '101010') == 4)
        self.assertTrue(levenshtein_deletion_distance('11001', '100010') == 3)
        self.assertTrue(levenshtein_deletion_distance('1010', '11010') == 1)
        self.assertTrue(levenshtein_deletion_distance('110001', '0000010') == 5)
        self.assertTrue(levenshtein_deletion_distance('110000', '0100010') == 3)


class TestLCS(unittest.TestCase):
    def test_random(self):
        for i in range(10):
            w1 = ''.join([str(x) for x in np.random.choice([0, 1], size=np.random.randint(4, 10))])
            w2 = ''.join([str(x) for x in np.random.choice([0, 1], size=np.random.randint(4, 10))])
            self.assertEqual(longest_common_subsequence(w1, w2), pylcs.lcs_sequence_length(w1, w2))

    def test_concrete(self):
        self.assertTrue(longest_common_subsequence('', '') == 0)
        self.assertTrue(longest_common_subsequence('', '1') == 0)
        self.assertTrue(longest_common_subsequence('1', '') == 0)
        self.assertTrue(longest_common_subsequence('1', '0') == 0)
        self.assertTrue(longest_common_subsequence('0', '111') == 0)
        self.assertTrue(longest_common_subsequence('1111', '1') == 1)
        self.assertTrue(longest_common_subsequence('110001', '1000101') == 5)
        self.assertTrue(longest_common_subsequence('1111', '101010') == 3)
        self.assertTrue(longest_common_subsequence('11001', '100010') == 4)
        self.assertTrue(longest_common_subsequence('1010', '11010') == 4)
        self.assertTrue(longest_common_subsequence('110001', '0000010') == 4)
        self.assertTrue(longest_common_subsequence('110000', '0100010') == 5)
        self.assertTrue(longest_common_subsequence('100010', '110001') == 5)
        self.assertTrue(longest_common_subsequence('101010', '111111') == 3)
        self.assertTrue(longest_common_subsequence('11010', '11001') == 4)
        self.assertTrue(longest_common_subsequence('0010010', '110001') == 4)

