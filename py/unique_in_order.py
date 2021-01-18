# https://www.codewars.com/kata/54e6533c92449cc251001667/

def unique_in_order(s):
  arr = [i for i in s]
  newArr = []

  for index, elem in enumerate(arr):
    if(index + 1 != len(arr)):
      if (elem == arr[index + 1]):
        continue
    newArr.append(elem)

  return newArr
