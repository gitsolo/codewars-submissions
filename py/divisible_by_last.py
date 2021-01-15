# https://www.codewars.com/kata/5a2809dbe1ce0e07f800004d

def divisible_by_last(n):
  arr = [int(i) for i in str(n)]

  return [False if arr[index - 1] == 0 or index - 1 == -1 else elem % arr[index - 1] == 0 for index, elem in enumerate(arr)]
