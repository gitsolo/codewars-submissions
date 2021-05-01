def compute_sum(n):
  arr = []

  for i in range(0, n + 1):
    num = str(i)

    if (len(num) == 1):
      arr.append(i)
    else:
      for j in num:
        arr.append(int(j))

  return sum(arr)
