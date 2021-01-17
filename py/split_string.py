# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

def solution(s):
  return [s[i] + '_' if (i + 1 == len(s)) else s[i] + s[i + 1] for i in range(0, len(s), 2)]
