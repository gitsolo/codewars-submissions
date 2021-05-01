def is_merge(s, part1, part2):
  if (part1 + part2 == s):
    return True

  if (sorted(s) != sorted(part1 + part2)):
    return False

  def r(lis):
    arr = []
    for i in lis:
      try:
        arr.append(s.index(i, 0 if len(arr) == 0 else arr[-1]))
      except:
        arr.append(0)
    return arr

  finalArr = [r(part1), r(part2)]

  return all([sorted(i) == i for i in finalArr])
