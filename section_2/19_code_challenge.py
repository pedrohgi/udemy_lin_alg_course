# Is the dot product commutative for vectors?

# Generate two 100 elements random row vectors
# Compute the dot products a with b and b with a
# generate 2-elements interger row vectors, repeat.

import scipy as sp
import numpy as np

a = np.random.rand(2)
b = np.random.rand(2)

left_dot = np.transpose(a)@b
right_dot = np.transpose(b)@a

print(left_dot, right_dot)
print("are they equal?", True if left_dot==right_dot else False)

