# https://www.codewars.com/kata/5300901726d12b80e8000498/train/python

def fizzbuzz(n):
  arr = []

  for i in range(1, n + 1):
    if (i % 3 == 0 and i % 5 == 0):
      arr.append('FizzBuzz')
    elif (i % 3 == 0):
      arr.append('Fizz')
    elif (i % 5 == 0):
      arr.append('Buzz')
    else:
      arr.append(i)

  return arr
