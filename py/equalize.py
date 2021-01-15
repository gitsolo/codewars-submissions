# https://www.codewars.com/kata/580a1a4af195dbc9ed00006c

def equalize(arr):
  newArr = []

  for i in arr:
    k = i - arr[0]

    if (k < 0):
      newArr.append(str(k))
      continue

    newArr.append(f"+{k}")

  return newArr
