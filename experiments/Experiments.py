#
#   @file : Experiments.py
#   @date : 05 March 2024
#   @authors : Orel Adivi and Daniel Noor
#
import time
import numpy as np
from tqdm import tqdm
from typing import Callable

from codes.RandomCode import RandomCode
from codes.GreedyCode import GreedyCode
from codes.LinSpaceCode import LinSpaceCode
from codes.LogSpaceCode import LogSpaceCode
from codes.RepetitionCode import RepetitionCode
from codes.VTRepetitionCode import VTRepetitionCode
from codes.VTRepetitionNaryCode import VTRepetitionNaryCode
from codes.RandomGreedyCode import RandomGreedyCode

RES_FILE = "./artifacts/results.csv"
LOGSPACE_PATTERN_FILE = "./artifacts/logspace_patterns.csv"
GREEDY_RANDOM_OPTIONS_FILE = "./artifacts/greedy_random_options.csv"
VTREPETITION_TUNING_FILE = "./artifacts/vtrepetition_tuning.csv"
VTREPETITIONNARY_TUNING_FILE = "./artifacts/vtrepetitionnary_tuning.csv"


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


def run_experiment1() -> None:
    lengths = list(range(50, 550, 50))
    codes = [
        (lambda length: RandomCode(length=length), 'RandomCode'),
        (lambda length: GreedyCode(length=length), 'GreedyCode'),
        (lambda length: LinSpaceCode(length=length), 'LinSpaceCode'),
        (lambda length: LogSpaceCode(length=length), 'LogSpaceCode'),
        (lambda length: RepetitionCode(length=length), 'RepetitionCode'),
        (lambda length: VTRepetitionCode(length=length), 'VTRepetitionCode'),
        (lambda length: VTRepetitionNaryCode(length=length), 'VTRepetitionNaryCode'),
        (lambda length: RandomGreedyCode(length=length), 'RandomGreedyCode'),
    ]

    print(f'=== Performing experiment #1:')
    with open(RES_FILE, "w") as f:
        f.write('"length"')
        for _, title in codes:
            f.write(f',"{title} (deletions)","{title} (seconds)"')
        f.write('\n')
        for length in lengths:
            print(f'Now calculating length={length}:')
            f.write(f'{length}')
            for code, _ in tqdm(codes):
                deletions, seconds = measure_code(lambda: code(length))
                f.write(f',{deletions},{seconds}')
            f.write('\n')
    print(f'Done!\n')


def run_experiment2() -> None:
    pass


def run_experiment3() -> None:
    pass


def run_experiment4() -> None:
    pass


if __name__ == '__main__':
    run_experiment1()
    run_experiment2()
    run_experiment3()
    run_experiment4()
