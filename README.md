# Low-rate Deletion Correcting Code

<!-- tags -->
<!-- logo -->

## About the Project

"Random-Greedy" is the short name for this project, aiming to generate and compare low-rate deletion correcting codes.
This short name is also the name of out main artifact, a simple algorithm that provides better deletion correcting
abilities, compared to other codes we checked. In the project, eight methodologies for generating codes (some of them
with meta-parameters) were created, and compared for their deletion correcting abilities (so no insertions nor
substitutions are allowed). The codes are low-rate, so each codeword has $n$ bits total and of them $O(log(n))$ are information bits. We achieve this by generating the codes with the number of codewords to be equal to the codeword length. The full description of the project is available in the
[project report PDF file](https://github.com/orel-adivi/Random-Greedy/blob/master/report/report.pdf).

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
- [`RepetitionCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/RepetitionCode.py) – this class generates code ???
- [`VTRepetitionCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/VTRepetitionCode.py) – this class generates code ???
`m`
- [`VTRepetitionNaryCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/VTRepetitionNaryCode.py) – this class generates code ???
`m`
`q`
- [`RandomGreedyCode`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/RandomGreedyCode.py) – this class generates code ???
`options`

All these classes are derived from the class
[`Code`](https://github.com/orel-adivi/Random-Greedy/blob/main/codes/Code.py), which allows the selection of codeword
length in the construction (with the parameter `length`) and provides the methods `encode` (for encoding a value),
`decode` (for decoding a codeword), and max_deletions (for calculating the maximal number of
deletions allowed).


### Utilities

todo

## Experiments

todo

## Project Engineering

todo

Please feel free to contact us with any questions you have about this project.
