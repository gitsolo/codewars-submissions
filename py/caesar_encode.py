# https://www.codewars.com/kata/55ec55323c89fc5fbd000019

def single_word(word: str, key: int):
  newArr = []
  for i in word:
    k = ord(i) + key
    realShift = k if (k <= 122) else k - 26
    newArr.append(chr(realShift))
  return ''.join(newArr)


def get_key(shift: int):
  return shift if (shift < 26) else shift % 26


def caesar_encode(phrase, shift):
  arr = phrase.lower().split(' ')
  return ' '.join([single_word(elem, get_key(shift + index)) for index, elem in enumerate(arr)])
