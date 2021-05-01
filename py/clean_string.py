def clean_string(s):
  arr = []

  for i in s:
    if (i == '#'):
      arr.pop() if len(arr) != 0 else {}
    else:
      arr.append(i)

  return ''.join(arr)
