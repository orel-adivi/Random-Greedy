# Low-rate Deletion Correcting Code

<!-- tags -->
<!--
[![Sanity Check - Build](https://github.com/orel-adivi/CorSys/actions/workflows/build.yml/badge.svg)](https://github.com/orel-adivi/CorSys/actions/workflows/build.yml)
[![Run all Benchmarks - Testing](https://github.com/orel-adivi/CorSys/actions/workflows/benchmarks.yml/badge.svg)](https://github.com/orel-adivi/CorSys/actions/workflows/benchmarks.yml)
[![Check Style (Flake8) - Style](https://github.com/orel-adivi/CorSys/actions/workflows/style.yml/badge.svg)](https://github.com/orel-adivi/CorSys/actions/workflows/style.yml)
[![Vulnerabilities Check (CodeQL) - Security](https://github.com/orel-adivi/CorSys/actions/workflows/vulnerabilities.yml/badge.svg)](https://github.com/orel-adivi/CorSys/actions/workflows/vulnerabilities.yml)
[![GitHub](https://img.shields.io/github/license/orel-adivi/CorSYs)](https://github.com/orel-adivi/CorSys/blob/main/LICENSE)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/orel-adivi/CorSys)](https://github.com/orel-adivi/CorSys/releases)
[![GitHub all releases](https://img.shields.io/github/downloads/orel-adivi/CorSys/total)](https://github.com/orel-adivi/CorSys/releases)
[![GitHub repo size](https://img.shields.io/github/repo-size/orel-adivi/CorSys)](https://github.com/orel-adivi/CorSys)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Forel-adivi.github.io%2FCorSys%2F)](https://orel-adivi.github.io/CorSys/)
-->

[![logo](/website/logo.png)](https://github.com/orel-adivi/Random-Greedy)


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
available in the [`artifacts`](https://github.com/orel-adivi/Random-Greedy/tree/main/artifacts) folder. Furthermore,
for testing the [`utils`](https://github.com/orel-adivi/Random-Greedy/tree/main/utils) folder files, we wrote a test file
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

### Design and Development

The project was designed in accordance with the object-oriented programming (OOP) principles. The project was written
using PyCharm Professional and was managed using [GitHub](https://github.com/orel-adivi/Random-Greedy).

<!-- For documentation, a
[website](https://orel-adivi.github.io/Random-Greedy/) is available and a
[SUPPORT.md](https://github.com/orel-adivi/Random-Greedy/blob/main/SUPPORT.md) file was written. -->

### Continuous Integration

In order to ensure the correctness of commits sent to the GitHub server, a continuous integration pipeline was set.
These checks are run automatically for each pull request and each push. The following actions were set:

1) **[Run experiments](https://github.com/orel-adivi/Random-Greedy/actions/workflows/experiments.yml)** - this action
runs all the experiments and generates the related figures.
2) **[Run unittests](https://github.com/orel-adivi/Random-Greedy/actions/workflows/tests.yml)** - this action runs all
the unittests for the [`utils`](https://github.com/orel-adivi/Random-Greedy/tree/main/utils) folder files.
3) **[Style check](https://github.com/orel-adivi/Random-Greedy/actions/workflows/style.yml)** - this action performs
basic checks of the `Python` files for detecting syntax errors.
4) **[Vulnerability check](https://github.com/orel-adivi/Random-Greedy/actions/workflows/vulnerabilities.yml)** - this
action help managing the `Python` code and its dependencies.
5) **[Dependency review](https://github.com/orel-adivi/Random-Greedy/actions/workflows/dependency-review.yml)** - this
action help managing the `Python` code dependencies for pushes.
6) **[Dependabot](https://github.com/orel-adivi/Random-Greedy/blob/main/.github/dependabot.yml)** - this action helps
update the versions of the dependencies.

<!--
website
latex

6) **[Website]()** - the
[Random-Greedy website](https://orel-adivi.github.io/Random-Greedy/) is updated with the current information.
-->

For the relevant actions, the checks were run in all the supported Python version `CPython 3.10` and on both Windows
(Windows Server 2022) and Linux (Ubuntu 20.04).


Please feel free to contact us with any questions you have about this project.
