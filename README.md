# CAM_Project

Link to paper: https://ieeexplore.ieee.org/abstract/document/9954058?casa_token=fyixySEJF_EAAAAA:Rzo6GWpdc5dvKL-UjuqQn9eDh0XFK5jzQE0O0CG8I_gCW1LSPc_wvaZHC2iGgw3EL9TglSlWlzBWd1w  

DONE:  
* Created random code generator, for n=100 it seems to be able to handle no more than 18/19 deletions  
* Created a simple greedy xor-based code generator, for n=100 it yields worse results than the random code (14 deletions)  
* Created a code generator which creates words from increasing runs of 0's and 1's (as well as the all-0 and all-1 words)
* Improved the previous generator with np.logspace, seems to allow n/4 deletions

TODO:
* Go over the relevant parts in the given paper  
* Create more generators
