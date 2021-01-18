# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

from functools import reduce


def persistence(n):
  if (n < 10):
    return 0

  def f(x): return reduce(lambda x, y: x * y, [int(i) for i in str(x)])

  num = n
  i = 1

  while (f(num) >= 10):
    num = f(num)
    i = i + 1

  return i
