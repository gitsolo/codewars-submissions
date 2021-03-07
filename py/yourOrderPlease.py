import re


def order(sentence):
  if sentence == '':
    return ''

  line = sentence.split(' ')
  positions = [int(re.findall("\d", i)[0]) - 1 for i in line]

  arr = list(range(0, len(line)))

  for i, j in zip(positions, line):
    arr[i] = j

  return ' '.join(arr)
