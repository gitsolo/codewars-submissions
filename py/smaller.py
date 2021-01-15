# https://www.codewars.com/kata/56a1c074f87bc2201200002e

def smaller(arr):
  return [len([i for i in arr[index:] if i < elem]) for index, elem in enumerate(arr)]
