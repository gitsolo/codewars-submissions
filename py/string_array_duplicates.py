# https://www.codewars.com/kata/59f08f89a5e129c543000069/train/python

def dup(arr):
  res = []

  for i in arr:
    newS = []
    for index, letter in enumerate(i):
      if(index != len(i) - 1):
        if (letter == i[index + 1]):
          continue
        else:
          newS.append(letter)
          continue
      newS.append(letter)
    res.append(''.join(newS))

  return res
