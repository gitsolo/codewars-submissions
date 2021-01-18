# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

def count(s):
  obj = {}

  for i in s:
    if (obj.get(i)):
      obj[i] = obj[i] + 1
      continue
    obj.setdefault(i, 1)

  return obj
