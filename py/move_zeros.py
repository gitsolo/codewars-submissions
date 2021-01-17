# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(arr):
  newArr = []

  for i in arr:
    if ((type(i) != type(10) and type(i) != type(10.0)) or i != 0.0):
      newArr.append(i)
      continue

  return newArr + ([0] * (len(arr) - len(newArr)))
