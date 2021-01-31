# https://www.codewars.com/kata/595bbea8a930ac0b91000130/train/python

def calculate_1RM(w, r):
  if (r == 1):
    return w

  if (r == 0):
    return 0

  return round(max([
      w * (1 + (r / 30)),
      (100 * w) / (101.3 - (2.67123 * r)),
      w * (r ** 0.10),
  ]))
