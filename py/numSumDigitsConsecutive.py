# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python

def isReq(num):
  arr = [int(i) for i in str(num)]
  total = 0

  for index, elem in enumerate(arr):
    total = total + (elem ** (index + 1))

  return total == num


def sum_dig_pow(a, b):
  return [i for i in range(a, b + 1) if isReq(i)]
