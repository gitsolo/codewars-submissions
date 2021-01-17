from math import *


def count(n):
  # Kamenetsky’s formula
  return floor(n * log10(n / e) + log10(2 * pi * n) / 2) + 1


# another => ceil(sum([log10(i) for i in range(1, n + 1)]))
# log(a * b) = log(a) + log(b)
