#
#   @file : Experiments.py
#   @date : 05 March 2024
#   @authors : Orel Adivi and Daniel Noor
#
import time
import numpy as np
from typing import Callable


def measure_code(code_constructor: Callable) -> [int, int]:
    deletion_results = []
    time_results = []
    for _ in range(3):
        start_time = time.time()
        deletions = code_constructor().max_deletions()
        end_time = time.time()
        deletion_results.append(deletions)
        time_results.append(end_time - start_time)
    return tuple([max(deletion_results), np.average(time_results)])


def calculate_m_value(length: int) -> int:
    log_l = int(np.ceil(np.log2(length)))
    return log_l + int(np.ceil(np.log2(log_l))) + 1


if __name__ == '__main__':
    cc = 1
    measure_code(cc)
