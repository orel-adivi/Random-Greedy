# Low-rate Deletion Correcting Code

<!-- tags -->
<!-- logo -->

## About the Project

"Random-Greedy" is the short name for this project, aiming to generate and compare low-rate deletion correcting codes.
This short name is also the name of out main artifact, a simple algorithm that provides better deletion correcting
abilities, compared to other codes we checked. In the project, eight methodologies for generating codes (some of them
with meta-parameters) were created, and compared for their deletion correcting abilities (so no insertions nor
substitutions are allowed). The codes are low-rate, so the number of codewords generated for each code is in
$O(log(n))$ for $n$ to be the maximal possible code space. Specifically, we generated the codes with the number of
codewords to be equal to the codeword length. The full description of the project is available in the
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
with 2 options for each selection point, and using it, the following code can be used:

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

todo

### Utilities

todo

## Experiments

todo

## Project Engineering

todo

Please feel free to contact us with any questions you have about this project.
