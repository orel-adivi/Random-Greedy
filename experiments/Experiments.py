#
#   @file : Experiments.py
#   @date : 13 April 2024
#   @authors : Orel Adivi and Daniel Noor
#
import sys
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

BASE_DIRECTORY = './artifacts'


def measure_code(code_constructor: Callable, repetitions=3) -> [Code, int, int]:
    """This function performs an experiment on with a given code."""
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
    """This function calculates the relevant m value for the given length."""
    log_l = int(np.ceil(np.log2(length)))
    return log_l + int(np.ceil(np.log2(log_l))) + 1


def run_experiment1() -> None:
    """In this experiment, the codes that provide as least n codewords are compared."""
    lengths = list(range(50, 551, 50))
    codes = [
        (lambda ln: RandomCode(length=ln), 'RandomCode'),
        (lambda ln: GreedyCode(length=length), 'GreedyCode'),
        (lambda ln: RepetitionCode(length=ln), 'RepetitionCode'),
        (lambda ln: VTRepetitionCode(length=ln, m=calculate_m_value(ln)), 'VTRepetitionCode'),
        (lambda ln: VTRepetitionNaryCode(length=ln, m=calculate_m_value(ln), q=4), 'VTRepetitionNaryCode'),
        (lambda ln: RandomGreedyCode(length=ln, options=2), 'RandomGreedyCode'),
    ]

    print(f'=== Performing experiment #1:')
    with open(BASE_DIRECTORY + '/experiment1.csv', 'w') as f:
        f.write('"length"')
        for _, title in codes:
            f.write(f',"{title} (deletions)","{title} (seconds)"')
        f.write('\n')
        for length in tqdm(lengths):
            f.write(f'{length}')
            for code, _ in codes:
                code, deletions, seconds = measure_code(lambda: code(length))
                assert len(code.codewords) == length
                for codeword in code.codewords:
                    assert len(codeword) == length
                f.write(f',{deletions},{seconds}')
            f.write('\n')


def run_experiment2() -> None:
    """In this experiment, the abilities of different codes to provide codewords are compared."""
    lengths = list(range(50, 551, 50))
    codes = [
        (lambda ln: LinSpaceCode(length=ln), 'LinSpaceCode'),
        (lambda ln: LogSpaceCode(length=ln, pattern_false='0', pattern_true='1'),
         'LogSpaceCode (shorter pattern)'),
        (lambda ln: LogSpaceCode(length=ln, pattern_false='00', pattern_true='11'),
         'LogSpaceCode (longer pattern)'),
        (lambda ln: RandomGreedyCode(length=ln, options=2), 'RandomGreedyCode'),
    ]

    print(f'\n=== Performing experiment #2:')
    with open(BASE_DIRECTORY + '/experiment2.csv', 'w') as f:
        f.write('"length"')
        for _, title in codes:
            f.write(f',"{title} (deletions)","{title} (seconds)",{title} (codewords)')
        f.write('\n')
        for length in tqdm(lengths):
            f.write(f'{length}')
            for code, _ in codes:
                code, deletions, seconds = measure_code(lambda: code(length))
                assert len(code.codewords) <= length
                for codeword in code.codewords:
                    assert len(codeword) == length
                f.write(f',{deletions},{seconds},{len(code.codewords)}')
            f.write('\n')


def run_experiment3() -> None:
    """This experiment compares different choices of 'q' parameter (base) for VTRepetitionNaryCode."""
    lengths = list(range(50, 251, 50))
    codes = [
        (lambda ln: VTRepetitionCode(length=ln, m=calculate_m_value(ln)),
         'VTRepetitionCode'),
        (lambda ln: VTRepetitionNaryCode(length=ln, m=calculate_m_value(ln), q=4),
         'VTRepetitionNaryCode (4-ary)'),
        (lambda ln: VTRepetitionNaryCode(length=ln, m=calculate_m_value(ln), q=8),
         'VTRepetitionNaryCode (8-ary)'),
    ]

    print(f'\n=== Performing experiment #5:')
    with open(BASE_DIRECTORY + '/experiment3.csv', 'w') as f:
        f.write('"length"')
        for _, title in codes:
            f.write(f',"{title} (deletions)","{title} (seconds)"')
        f.write('\n')
        for length in tqdm(lengths):
            f.write(f'{length}')
            for code, _ in codes:
                code, deletions, seconds = measure_code(lambda: code(length))
                assert len(code.codewords) == length
                for codeword in code.codewords:
                    assert len(codeword) == length
                f.write(f',{deletions},{seconds}')
            f.write('\n')


def run_experiment4() -> None:
    """This experiment compares different choices of 'option' parameter for RandomGreedyCode."""
    lengths = list(range(50, 551, 50))
    codes = [
        (lambda ln: RandomGreedyCode(length=ln, options=1), 'RandomGreedyCode (1 options)'),
        (lambda ln: RandomGreedyCode(length=ln, options=2), 'RandomGreedyCode (2 options)'),
        (lambda ln: RandomGreedyCode(length=ln, options=3), 'RandomGreedyCode (3 options)'),
        (lambda ln: RandomGreedyCode(length=ln, options=4), 'RandomGreedyCode (4 options)'),
        (lambda ln: RandomGreedyCode(length=ln, options=5), 'RandomGreedyCode (5 options)'),
    ]

    print(f'\n=== Performing experiment #4:')
    with open(BASE_DIRECTORY + '/experiment4.csv', 'w') as f:
        f.write('"length"')
        for _, title in codes:
            f.write(f',"{title} (deletions)","{title} (seconds)"')
        f.write('\n')
        for length in tqdm(lengths):
            f.write(f'{length}')
            for code, _ in codes:
                code, deletions, seconds = measure_code(lambda: code(length))
                assert len(code.codewords) == length
                for codeword in code.codewords:
                    assert len(codeword) == length
                f.write(f',{deletions},{seconds}')
            f.write('\n')


if __name__ == '__main__':
    if len(sys.argv) > 2:
        BASE_DIRECTORY = sys.argv[-1]
    #run_experiment1()
    #run_experiment2()
    #run_experiment3()
    run_experiment4()
