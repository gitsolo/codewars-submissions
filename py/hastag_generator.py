# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

def generate_hashtag(s):
  if (s.strip() == '' or len(s) > 140):
    return False

  arr = s.strip().split(' ')
  res = '#'

  for i in arr:
    res = res + i.capitalize()

  return res
