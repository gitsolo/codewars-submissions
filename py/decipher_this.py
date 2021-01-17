# https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python

import re


def decipher_this(string):
  arrWord = string.split(' ')
  res = []

  for i in arrWord:
    arr = re.split('(\D+)', i)
    firstLetter = chr(int(arr[0]))

    if(len(arr) > 1):
      if (len(arr[1]) == 1):
        res.append(firstLetter + arr[1])
      elif (len(arr[1]) == 2):
        res.append(firstLetter + arr[1][-1] + arr[1][0])
      else:
        res.append(firstLetter + arr[1][-1] + arr[1][1:-1] + arr[1][0])
    else:
      res.append(firstLetter)

  return ' '.join(res)
