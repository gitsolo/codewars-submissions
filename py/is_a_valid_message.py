# https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc

import re


def is_a_valid_message(message):
  arr = list(filter(None, re.split(r'(\D+)', message)))

  print(arr)

  if (len(arr) % 2 != 0):
    return False

  try:
    return(all([len(arr[i]) == int(arr[i - 1]) for i in range(1, len(arr), 2)]))
  except:
    return False
