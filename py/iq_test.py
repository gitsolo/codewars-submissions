# https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
  arr = [int(i) % 2 == 0 for i in numbers.split(' ')]
  return (arr.index(not (arr.count(True) > arr.count(False))) + 1)
