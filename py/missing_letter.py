# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

# def find_missing_letter(chars):
#   return chr(list(set(range(ord(chars[0]), ord(chars[-1]) + 1)).difference([ord(i) for i in chars]))[0])


def find_missing_letter(chars):
  arr = [ord(i) for i in chars]

  for i, elem in enumerate(range(ord(chars[0]), ord(chars[-1]) + 1)):
    if (arr[i] != elem):
      return chr(elem)
