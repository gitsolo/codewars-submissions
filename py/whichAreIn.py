# https://www.codewars.com/kata/550554fd08b86f84fe000a58/solutions/python

def in_array(arr1, arr2):
  arr = []

  for i in arr1:
    for j in arr2:
      if (i in j):
        arr.append(i)

  return sorted(set(arr))
