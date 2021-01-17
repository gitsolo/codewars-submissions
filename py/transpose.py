# https://www.codewars.com/kata/52fba2a9adcd10b34300094c/train/python

def transpose(matrix):
  arr = []

  for i in range(0, len(matrix[0])):
    subArr = []
    for j in range(0, len(matrix)):
      subArr.append(matrix[j][i])

    arr.append(subArr)

  return arr
