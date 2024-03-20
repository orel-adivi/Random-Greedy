#
#   @file : Experiments.py
#   @date : 05 March 2024
#   @authors : Orel Adivi and Daniel Noor
#
import time
import numpy as np
from tqdm import tqdm
from typing import Callable

from codes.Code import Code
from codes.RandomCode import RandomCode
from codes.GreedyCode import GreedyCode
from codes.LinSpaceCode import LinSpaceCode
from codes.LogSpaceCode import LogSpaceCode
from codes.RepetitionCode import RepetitionCode
from codes.VTRepetitionCode import VTRepetitionCode
from codes.VTRepetitionNaryCode import VTRepetitionNaryCode
from codes.RandomGreedyCode import RandomGreedyCode

RES_FILE = "./artifacts/experiment1_results.csv"
SPARSE_FILE = "./artifacts/experiment2_results.csv"
LOGSPACE_PATTERN_FILE = "./artifacts/experiment3_results.csv"
GREEDY_RANDOM_OPTIONS_FILE = "./artifacts/experiment4_results.csv"
VTREPETITIONNARY_TUNING_FILE = "./artifacts/experiment5_results.csv"


def measure_code(code_constructor: Callable, repetitions=3) -> [Code, int, int]:
    assert repetitions > 0
    deletion_results = []
    time_results = []
    code = None
    for _ in range(repetitions):
        start_time = time.time()
        code = code_constructor()
        end_time = time.time()
        deletions = code.max_deletions()
        deletion_results.append(deletions)
        time_results.append(end_time - start_time)
    return tuple([code, max(deletion_results), np.average(time_results)])


def calculate_m_value(length: int) -> int:
    log_l = int(np.ceil(np.log2(length)))
    return log_l + int(np.ceil(np.log2(log_l))) + 1


def run_experiment1() -> None:
    lengths = list(range(50, 550, 50))
    codes = [
        (lambda length: RandomCode(length=length), 'RandomCode'),
        (lambda length: RepetitionCode(length=length), 'RepetitionCode'),
        (lambda length: VTRepetitionCode(length=length, m=calculate_m_value(length)), 'VTRepetitionCode'),
        (lambda length: VTRepetitionNaryCode(length=length, m=calculate_m_value(length), q=4), 'VTRepetitionNaryCode'),
        (lambda length: RandomGreedyCode(length=length, options=2), 'RandomGreedyCode'),
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
                code, deletions, seconds = measure_code(lambda: code(length))
                assert len(code.codewords) == length
                for codeword in code.codewords:
                    assert len(codeword) == length
                f.write(f',{deletions},{seconds}')
            f.write('\n')
            print(f'Done!\n')


def run_experiment2() -> None:
    lengths = list(range(100, 151, 10))
    codes = [
        (lambda length: RandomCode(length=length), 'RandomCode'),
        (lambda length: GreedyCode(length=length), 'GreedyCode'),
        #(lambda length: LinSpaceCode(length=length), 'LinSpaceCode'),
        #(lambda length: LogSpaceCode(length=length, pattern_false='0', pattern_true='1'), 'LogSpaceCode'),
        (lambda length: RepetitionCode(length=length), 'RepetitionCode'),
        (lambda length: RandomGreedyCode(length=length, options=2), 'RandomGreedyCode'),
    ]

    print(f'=== Performing experiment #2:')
    with open(SPARSE_FILE, "w") as f:
        f.write('"length"')
        for _, title in codes:
            f.write(f',"{title} (deletions)","{title} (seconds)",{title} (codewords)')
        f.write('\n')
        for length in lengths:
            print(f'Now calculating length={length}:')
            f.write(f'{length}')
            for code, _ in tqdm(codes):
                code, deletions, seconds = measure_code(lambda: code(length))
                codewords = len(code.codewords)
                assert codewords <= length
                for codeword in code.codewords:
                    assert len(codeword) == length
                f.write(f',{deletions},{seconds},{codewords}')
            f.write('\n')
            print(f'Done!\n')


def run_experiment3() -> None:
    # log pattern
    pass


def run_experiment4() -> None:
    # greedy random options
    pass


def run_experiment5() -> None:
    # vtrepetitionnary
    pass


if __name__ == '__main__':
    #run_experiment1()
    run_experiment2()
    run_experiment3()
    run_experiment4()
    run_experiment5()
