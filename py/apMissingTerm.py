def getOddaDiff(arr):
  oddOne = 0
  other = 0

  for i in list(set(arr)):
    if arr.count(i) == 1:
      oddOne = i
    else:
      other = i

  return [oddOne, other]


def find_missing(ap):
  arrDiff = [ap[i] - ap[i - 1] for i in range(1, len(ap))]

  oddOne, commonDiff = getOddaDiff(arrDiff)

  return ap[arrDiff.index(oddOne)] + commonDiff
