# https://www.codewars.com/kata/56b0f6243196b9d42d000034

def sum_factorial(lst):
  arr = sorted(lst)

  result = 0
  prod = 1

  for i in range(1, arr[-1] + 1):
    prod = prod * i
    if (i in arr):
      result = result + prod

  return result


# NOTE: eg: [4,6], 1*2*3*4 already calculated, why to calculate again
