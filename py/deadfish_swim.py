# https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python

def parse(data):
  val = 0
  arr = []

  for i in data:
    if (i == 'i'):
      val = val + 1
    elif (i == 'd'):
      val = val - 1
    elif (i == 's'):
      val = val ** 2
    elif (i == 'o'):
      arr.append(val)

  return arr
