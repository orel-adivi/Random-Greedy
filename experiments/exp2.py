import timeit

# import matplotlib.pyplot as plt
import timeit
import numpy as np

from codes.GreedyCode import GreedyCode
from codes.GreedyRandomCode import GreedyRandomCode
from codes.LinSpaceCode import LinSpaceCode
from codes.LogSpaceCode import LogSpaceCode
from codes.RandomCode import RandomCode
from codes.RepetitionCode import RepetitionCode
from codes.VTRepetitionCode import VTRepetitionCode
from codes.VTRepetitionNaryCode import VTRepetitionNaryCode


def calculate_max_deletions(constructor):
    res = []
    for _ in range(3):
        res.append(constructor().max_deletions())
    return max(res)


def calculate_runtime(constructor):
    return timeit.timeit(constructor().max_deletions(), number=3)


def calculate_m(l):
    log_l = int(np.ceil(np.log2(l)))
    return log_l + int(np.ceil(np.log2(log_l))) + 1


if __name__ == "__main__":
    y1 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=2)) for length in range(100, 600, 100)]
    print(y1)
    y2 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=3)) for length in range(100, 600, 100)]
    print(y2)
    y3 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=4)) for length in range(100, 600, 100)]
    print(y3)
    y4 = [calculate_max_deletions(lambda: GreedyRandomCode(length, options=5)) for length in range(100, 600, 100)]
    print(y4)
