# COT4500 Assignment 1

**Author**: Steven Grady  

## Overview  
In this assignment, I implement numerical methods for:  
1. **Double-precision floating-point conversion** (IEEE 754).  
2. **Three-digit chopping/rounding** arithmetic.  
3. **Error analysis** (absolute/relative errors).  
4. **Series convergence** (alternating series error bound).  
5. **Root-finding algorithms**:  
   - Bisection Method (approximates roots via interval halving).  
   - Newton-Raphson Method (uses derivatives for iterative root approximation).  

## Requirements  
- Python 3.12.5 (tested and compatible).  
- **No external libraries** required (see empty `requirements.txt`)  

## Run Instructions  
1. Clone the repository:  
```
   bash
   git clone https://github.com/ssgrady/cot-4500-Pro1.git
   cd cot-4500-Pro1
```
2. Execute the main script to print all answers:
```
python3 src/main/assignment_1.py
```
3. Run unit tests:
```
python3 -m unittest src/test/test_assignment1.py
```