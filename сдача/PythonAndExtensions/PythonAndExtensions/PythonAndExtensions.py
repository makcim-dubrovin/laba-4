import math
from random import random
from time import perf_counter
from superfastcode import fast_function



COUNT = 50000  # Change this value depending on the speed of your computer
DATA = [(random() - 0.5) * 3 for _ in range(COUNT)]

e = 2.7182818284590452353602874713527

def factorial(x):
	if x == 0 or x == 1:
		return 1
	return (x * factorial(x-1))

def function(x):
   # tanh_x = (cosh(x)/sinh(x) + sinh(x));
    tanh_x = math.pow(x, (-1)*4)/(factorial(4)*math.cos(x))
    return tanh_x

def test(fn, name):
    start = perf_counter()
    result = fn(DATA)
    duration = perf_counter() - start
    print('{} took {:.3f} seconds\n\n'.format(name, duration))

    #for d in result:
    #    assert -1 <= d <= 1, " incorrect values"

if __name__ == "__main__":
    print('Running benchmarks with COUNT = {}'.format(COUNT))

    test(lambda d: [fast_function(x) for x in d], '[fast_function(x) for x in d] (CPython C++ extension)')
    test(lambda d: [function(x) for x in d], '[function(x) for x in d] (Python implementation)')