# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
  def f(x): return sum([int(i) for i in str(x)])

  num = n

  while (f(num) >= 10):
    num = f(num)

  return f(num)
