# https://www.codewars.com/kata/58067088c27998b119000451

def reverse_factorial(num):
  prod = num

  for i in range(1, num + 1):
    prod = prod / i
    if (prod == 1):
      return f"{i}!"

    if (prod < 1):
      return 'None'
