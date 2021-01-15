# https://www.codewars.com/kata/52755006cc238fcae70000ed

def christmas_tree(height):
  newArr = []

  for i in range(0, height):
    space = ' ' * (height - i - 1)
    newArr.append(space + '*' * (1 + (i * 2)) + space)

  return('\n'.join(newArr))
