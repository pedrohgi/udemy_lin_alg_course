# test wheter the dot product sign is invariant to scalar multiplication 

# Generate two vectors in R3
# Generate two scalars
# Compute the dot product between vectors
# compute the dot product between the scaled vectors 

import scipy as sp
import numpy as np

v1 = np.array([1,2,3])
v2 = np.array([2,3,4])

scalar_list = [2]

for scalar in scalar_list:

  normal_dot = np.transpose(v1)@(v2)

  scaled_dot = np.transpose(v1*scalar)@ (v2*scalar)

  print('{:.2f}'.format(normal_dot), 
        '{:.2f}'.format(scaled_dot))
  print("Are both equal?",normal_dot == scaled_dot )
  print("Are the SIGNS equal?",np.sign(normal_dot) == np.sign(scaled_dot))
