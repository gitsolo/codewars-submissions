# https://www.codewars.com/kata/5266fba01283974e720000fa/train/python

def variance(arr):
  mean = sum(arr) / len(arr)
  return sum(map(lambda x: (x - mean) ** 2, arr)) / len(arr)
