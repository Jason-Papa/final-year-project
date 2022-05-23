# a is an integer vector
from numpy import *
from scipy.linalg import toeplitz

# a is an integer array
def negacyclic(a):
    r = zeros(len(a))
    r[0] = a[0]
    r[1:] = -a[-1:0:-1]
    return toeplitz(a,r)

# reference: https://github.com/KatinkaBou/Probabilistic-Bounds-On-Singular-Values-Of-Rotation-Matrices/blob/master/negacyclic_probabilistic_bound.py
# KatinkaBou github 


def sample_negacyclic(neg, number_of_samples = 1):
    samples = zeros(len(neg))
    for n in range(number_of_samples):
        choice = random.choice(len(neg), 2)
        print(choice)
        samples[n] = neg[choice[0]][choice[1]]
    return samples
# testing
n = negacyclic(array([1,2,3,4,5,6,7,8]))
print(n)
print(sample_negacyclic(n,7))


