# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

def high(x):
  arr = x.split(' ')
  newArr = []
  maxIndex = 0

  for i in range(0, len(arr)):
    f = sum([ord(j) - 96 for j in arr[i]])
    newArr.append(f)
    if (f > newArr[maxIndex]):
      maxIndex = i

  return arr[maxIndex]
