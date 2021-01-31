# https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python

def namelist(names):
  arr = list(map(lambda x: x['name'], names))
  length = len(arr)

  newArr = []

  if (length == 1):
    return arr[0]

  for i in range(0, length):
    if (i == (length - 1)):
      newArr.append(f" & {arr[i]}")
      continue

    if (i == length - 2):
      newArr.append(arr[i])
      continue

    newArr.append(f"{arr[i]}, ")

  return ''.join(newArr)
