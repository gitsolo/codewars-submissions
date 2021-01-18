# https://www.codewars.com/kata/55eeddff3f64c954c2000059/train/python

def sum_consecutives(arr):
  newArr = []

  i = 0
  while (i < len(arr)):
    nums = 1
    for j in arr[i + 1:]:
      if (j == arr[i]):
        nums = nums + 1
        i = i + 1
      else:
        break

    newArr.append(arr[i] * nums)
    nums = 0
    i = i + 1

  return newArr
