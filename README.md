# COT4500 Assignment 1

**Author**: Steven Grady  

## Overview  
In this assignment, I implement numerical calculus methods for:  
1. **Approximation method (specifically sqrt 2)** - a newton based iteration from an initial guess  
2. **Bisection Method** - generic bisection approach 
3. **Fixed-Point Iteration** - user-supplied g(x) to solve x = g(x)  
4. **Newson Raphson Method** - classical root-finding approach requiring f(x) and its derivative f'

## Requirements  
- Python 3.12.5 (tested and compatible).  
- **No external libraries** required aside from the standard library to run tests (see empty `requirements.txt`)

## Run Instructions  
1. Clone the repository using SSH:  
```
   git clone git@github.com:SSGrady/cot-4500-Pro1.git
   cd cot-4500-Pro1
```
2. Run the main script:
```
python3 src/main/assignment_1.py
```

This script shows each numerical method in action

3. Test using:
```
python3 -m unittest src/test/test_assignment_1.py
```

The tests verify correct iteration counts, final approximate roots, and correct convergence
