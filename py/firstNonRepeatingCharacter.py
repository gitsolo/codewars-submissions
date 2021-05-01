def first_non_repeating_letter(x):
  s = x.upper()
  for i, j in enumerate(s):
    if s.count(j) == 1:
      return x[i]

  return ''
