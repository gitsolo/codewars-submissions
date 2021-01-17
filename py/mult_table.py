# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python

def multiplication_table(size):
  arr = []

  for i in range(1, size + 1):
    subArr = []
    for j in range(1, size + 1):
      subArr.append(i * j)
    arr.append(subArr)

  return arr
