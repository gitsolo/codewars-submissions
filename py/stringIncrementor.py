import re


def increment_string(x):
  val = re.split('(\d+)', x)
  s = ''.join(val[0:] if len(val) == 1 else val[0:-2])
  num = val[-2] if len(val) >= 3 else '0'

  finalNum = int(num) + 1
  numDigits = len([int(i) for i in str(finalNum - 1)])

  if (len(num) == numDigits):
    return f"{s}{finalNum}"
  else:
    return f"{s}{str(finalNum).rjust(len(num), '0')}"
