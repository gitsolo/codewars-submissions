# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

def delete_nth(arr, n):
  newArr = []

  for i in arr:
    if (newArr.count(i) < n):
      newArr.append(i)

  return newArr
