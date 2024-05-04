# Low-rate Deletion Correcting Code

<!-- tags -->
<!-- logo -->

## About the Project

"Random-Greedy" is the short name for this project, aiming to generate and compare low-rate deletion correcting codes.
This short name is also the name of out main artifact, a simple algorithm that provides better deletion correcting
abilities, compared to other codes we checked. In the project, eight methodologies for generating codes (some of them
with meta-parameters) were created, and compared for their deletion correcting abilities (so no insertions nor
substitutions are allowed). The codes are low-rate, so each codeword has $n$ bits in total, and $O(log(n))$ of them are
information bits. We achieve this by generating the codes with the number of codewords to be equal to the codeword
length. The full description of the project is available in the
[project report PDF file](https://github.com/orel-adivi/Random-Greedy/blob/main/report/report.pdf).

This work is submitted as the final project in the course "Coding and Algorithms for Memories" (236379), at Taub Faculty
of Computer Science, Technion - Israel Institute of Technology. The project was written by Orel Adivi
`(orel.adivi [at] cs.technion.ac.il)` and Daniel Noor `(daniel.noor [at] cs.technion.ac.il)`, and under the supervision
of Daniella Bar-Lev and associate professor Eitan Yaakobi. The work was done in semester winter 2022-2023. The project
is released under MIT license.


## Usage

In order to generate the codes and use them, an installation of
[`CPython 3.10`](https://www.python.org/downloads/release/python-31014/) is required (the implementation is platform
independent, and was tested on both Windows and Linux).

The project uses `NumPy`, `Matplotlib`, `overrides`, `pylcs`, and `tqdm` Python libraries, which can be installed using
`Pip` package installer:

```bash
python -m pip install -r requirements.txt
```

Then, the codes can be imported, generated and used. For example, for generating `RandomGreedyCode` of length 100 and
with 2 options for each selection point, and using it, the following `Python` code can be used:

```python
import numpy as np
from codes.RandomGreedyCode import RandomGreedyCode

my_code = RandomGreedyCode(length=100, options=2)                   # generate the code
print(f'Codeword for the value 0:\t{my_code.encode(24)}')           # encode a value
print(f'Value for a codeword:\t{my_code.decode(np.zeros((100,)))}') # decode a codeword
print(f'Maximal number of deletions:\t{my_code.max_deletions()}')   # calculate deletion-distance
```

Other codes can be used similarly, as they share the interface defined in the
[`Code`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/Code.py) class.

### Codes

In this project, eight code classes are available:

- [`RandomCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/RandomCode.py) – this class generates code
by selecting serially random codewords that were not previously chosen.
- [`GreedyCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/GreedyCode.py) – this class generates code
selecting codewords to be as different as possible, by flipping bits during a serial traversal of the previously
- generated codewords.
- [`LinSpaceCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/LinSpaceCode.py) – this class generates 
code by repeating a pattern of alternating $0$-s and $1$-s with a length that increases linearly.
- [`LogSpaceCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/LogSpaceCode.py) – this class generates 
code by repeating a pattern of alternating `pattern_false`-s ($0$ is the default) and `pattern_true`-s ($1$ is the
default) with a length that increases linearly.
- [`RepetitionCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/RepetitionCode.py) – This class
generates code by taking all words of length $log(n)$ for $n$ the codeword length, and repeating each letter $n/log(n)$
times, thus generating codewords of length $n$.
- [`VTRepetitionCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/VTRepetitionCode.py) – this class
generates code by taking all words from $VT_0(m)$ for a given parameter `m` and multiplying each letter $n/m$ times.
- [`VTRepetitionNaryCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/VTRepetitionNaryCode.py) – this
class generates code by taking all words from $VT_0(m, q)$ for given parameter `m` and a base `q`, converting the words
to binary and multiplying each letter $n/m$ times.
- [`RandomGreedyCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/RandomGreedyCode.py) – this class
generates code serially by generating a set of codeword candidates of size `options`, and then selecting the candidate
with the largest distance from the previous codewords.

All these classes are derived from the class
[`Code`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/Code.py), which allows the selection of codeword
length in the construction (with the parameter `length`) and provides the methods `encode` (for encoding a value),
`decode` (for decoding a codeword), and max_deletions (for calculating the maximal number of
deletions allowed).


### Utilities

In the [`utils`](https://github.com/orel-adivi/Random-Greedy/tree/main/utils) folder, additional classes and functions,
used in the implementation of the different codes, are provided:

- [`LevenshteinDistance.py`](https://github.com/orel-adivi/Random-Greedy/blob/main/utils/LevenshteinDistance.py) – this
file contains a function that computes Levenshtein deletion distance between an expected string and a given string.
- [`LongestCommonSubsequence.py`](https://github.com/orel-adivi/Random-Greedy/blob/main/utils/LongestCommonSubsequence.py) – 
contains a function that computes the length of the longest common subsequence of given two strings (the function uses a
dynamic programming algorithm, and was replaced with the implementation in `pylcs`).
- [`VTCode.py`](https://github.com/orel-adivi/Random-Greedy/blob/main/utils/VTCode.py) – contains a VT code generator,
based on an implementation from a [`previous work`](https://github.com/shubhamchandak94/VT_codes/).


## Experiments

In order to compare the different code generation methodologies, and to tune meta-parameters for the relevant codes, we
wrote a `Python` script that runs these experiments, and another `Python` script that generates the figures from these
experiments. For running the two files, the following script can be executed:

```bash
python Experiments.py
python GenerateFigures.py
```

Running the experiments is expected to last several hours, so we also run this script in a
[GitHub action](https://github.com/orel-adivi/Random-Greedy/actions/workflows/tests.yml). Additionally, the results are
available in the [`artifacts`](https://github.com/orel-adivi/Random-Greedy/tree/main/artifacts) folder. Additionally,
for testing the [`utils`](https://github.com/orel-adivi/Random-Greedy/tree/main/utils) files folder, we wrote a test file
that can be executed using the following command:

```bash
python -m unittest Unittests.py
```

In the execution of the first two files, the following figures are generated:

- **[Figure 1](https://github.com/orel-adivi/Random-Greedy/blob/main/artifacts/figure1.png)** – this figure shows the
connection between the codeword length and maximal number of fixable deletions, for different codes.
- **[Figure 2](https://github.com/orel-adivi/Random-Greedy/blob/main/artifacts/figure2.png)** – this figure shows the
connection between the codeword length and maximal number of fixable deletions, for codes that can not generate the
desired number of codewords.
- **[Figure 3](https://github.com/orel-adivi/Random-Greedy/blob/main/artifacts/figure3.png)** – this figure shows the
connection between the codeword length and maximal number of fixable deletions, for `VTRepetitionNaryCode` in different
bases.
- **[Figure 4](https://github.com/orel-adivi/Random-Greedy/blob/main/artifacts/figure4.png)** – this figure shows the
connection between the codeword length and maximal number of fixable deletions, for `RandomGreedyCode` with different
number of options to choose from in each iteration.

The figures are described and discussed in detailed in the
[project report PDF file](https://github.com/orel-adivi/Random-Greedy/blob/main/report/report.pdf).


## Project Engineering

todo

Please feel free to contact us with any questions you have about this project.
