# https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python

def longest_repetition(s):
  res = ('', 0)
  i = 0

  while (i < len(s)):
    nums = 1
    for j in s[i + 1:]:
      if (j == s[i]):
        nums = nums + 1
        i = i + 1
      else:
        break

    mAx = res[1]
    if (mAx < nums):
      res = (s[i], nums)

    nums = 0
    i = i + 1

  return res
