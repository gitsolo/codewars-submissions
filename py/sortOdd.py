# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

def sort_array(arr):
  evenIndices = [index for index, elem in enumerate(arr) if elem % 2 == 0]
  sortedOdds = sorted([i for i in arr if i % 2 != 0])

  for i in evenIndices:
    sortedOdds.insert(i, arr[i])

  return sortedOdds
