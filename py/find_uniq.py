# https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
  if ((arr[0] != arr[1]) and (arr[0] == arr[2])):
    return arr[1]

  if ((arr[0] != arr[1]) and (arr[0] != arr[2])):
    return arr[0]

  if (arr[0] == arr[1]):
    for i in arr[2:]:
      if (i != arr[0]):
        return i
