# https://www.codewars.com/kata/59e19a747905df23cb000024/train/python

import re


def string_letter_count(s):
  newS = sorted(re.sub('[^a-z]', '', s.lower()))

  obj = {}

  for i in newS:
    if (i not in obj):
      obj[i] = 1
      continue

    obj[i] = obj[i] + 1

  return ''.join([f"{obj[i]}{i}" for i in obj.keys()])
