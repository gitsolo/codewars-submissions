def getMod(num):
  if num == 0:
    return None

  numDigits = len(str(num))
  return num % int(f"1{'0' * (numDigits - 1)}")


def expanded_form(num):
  arr = []

  prev = num
  x = getMod(num)

  while (x != None):
    arr.append(str(prev - x))
    prev = x
    x = getMod(x)

  return ' + '.join(arr)
