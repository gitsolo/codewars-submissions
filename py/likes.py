# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/

def likes(arr):
  s = 'like this'

  if (len(arr) == 0):
    return 'no one likes this'

  if (len(arr) == 1):
    return f"{arr[0]} likes this"

  if (len(arr) == 2):
    return f"{arr[0]} and {arr[1]} {s}"

  if (len(arr) == 3):
    return f"{arr[0]}, {arr[1]} and {arr[2]} {s}"

  return f"{arr[0]}, {arr[1]} and {len(arr) - 2} others {s}"
