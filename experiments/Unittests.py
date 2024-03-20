#
#   @file : Unittests.py
#   @date : 05 March 2024
#   @authors : Orel Adivi and Daniel Noor
#
import unittest
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

